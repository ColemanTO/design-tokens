// Deterministic frame capture: render(t) per frame -> JPEG -> ffmpeg pipe.
// Usage: node capture.js <out.mp4> [fps] [--stills t1,t2,...]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

(async () => {
  const dir = __dirname;
  const out = process.argv[2];
  const fps = parseInt(process.argv[3] || '30', 10);
  const stillsArg = process.argv.indexOf('--stills');
  const timings = JSON.parse(fs.readFileSync(path.join(dir, 'timings.json'), 'utf8'));
  const html = fs.readFileSync(path.join(dir, 'scenes.html'), 'utf8').replace('__TIMINGS__', JSON.stringify(timings));
  fs.writeFileSync(path.join(dir, 'scenes.built.html'), html);

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(dir, 'scenes.built.html'));
  await page.waitForLoadState('networkidle');
  await page.evaluate(async () => { await Promise.all(['400 80px Fraunces','600 80px Fraunces','400 30px "JetBrains Mono"','600 30px Inter'].map(f => document.fonts.load(f))); await document.fonts.ready; });
  const ok = await page.evaluate(() => document.fonts.check('600 80px Fraunces'));
  if (!ok) throw new Error('Fraunces failed to load');
  await page.waitForTimeout(500);
  const cdp = await page.context().newCDPSession(page);

  const shot = async () => Buffer.from((await cdp.send('Page.captureScreenshot', { format: 'jpeg', quality: 92 })).data, 'base64');

  if (stillsArg > -1) {
    const ts = process.argv[stillsArg + 1].split(',').map(Number);
    for (const t of ts) {
      await page.evaluate(t => window.render(t), t);
      fs.writeFileSync(path.join(dir, `still-${t}.jpg`), await shot());
    }
    await browser.close();
    return;
  }

  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const frames = Math.ceil(timings.total * fps);
  for (let i = 0; i < frames; i++) {
    await page.evaluate(t => window.render(t), i / fps);
    const buf = await shot();
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % (fps * 10) === 0) console.log(`frame ${i}/${frames}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('done', out);
})();
