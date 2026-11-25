# Design Impact Plan: overview video

Source files for a 2½-minute overview video of the [`design-impact-plan`](../../.claude/skills/design-impact-plan/) Claude Code skill. It has narration and an original music bed. Everything is generated from these files; nothing is recorded or licensed.

## Build

```bash
./build.sh            # default voice: af_heart
./build.sh am_michael # any Kokoro voice name
```

Outputs `design-impact-plan-overview.mp4` (1080p, 30 fps) and `design-impact-plan-soundtrack.mp3`. The full build takes a few minutes, most of it frame capture. On the first run it downloads the Kokoro model files (about 350 MB) into `models/`.

**Requirements:** Python 3, ffmpeg, and Node with Playwright and its Chromium (`npm i -D playwright && npx playwright install chromium` if you don't have them). The scene page loads the Fraunces font from Google Fonts, so the capture step needs network access.

## Files

| File | What it does |
|------|--------------|
| `script.json` | The narration, one entry per scene. Edit this to change what's said. |
| `make_vo.py` | Generates the narration with [Kokoro](https://github.com/thewh1teagle/kokoro-onnx) (open-weight text-to-speech, Apache-2.0), one clip per scene. Writes `vo.wav` and `timings.json` with each scene's start and end. |
| `make_music.py` | Synthesizes an original ambient bed with numpy: detuned saw pads, a soft sine pulse, and a plucked arpeggio over D major 9 → B minor 7 → G major 7 → A sus at 72 BPM, with convolution reverb. It uses fixed seeds, so the output is the same every time. |
| `scenes.html` | The visuals. Each scene's elements have a `data-at` value: the fraction of that scene's narration at which they appear. `render(t)` draws any moment in time. |
| `capture.js` | Loads `scenes.html` in headless Chromium, calls `render(t)` for every frame, and pipes screenshots to ffmpeg. Use `--stills 10,40` to check single frames. |
| `build.sh` | Runs everything: narration, music, the mix (voice compression, music ducking, −16 LUFS), frame capture, and muxing. |

## Common changes

- **Wording:** edit `script.json` and rebuild. Visual timing follows the new narration automatically.
- **Pronunciation:** respell the word in `script.json` (e.g. "C O two"). Only the spoken text changes, not what's on screen.
- **Voice:** pass a different Kokoro voice name to `build.sh`.
- **Music level:** change `volume=0.30` in the mix step of `build.sh`.
- **Music mood:** change `progression`, `BPM`, or the arpeggio `pattern` in `make_music.py`.
- **Visuals:** edit `scenes.html`, then preview with `node capture.js x.mp4 30 --stills <seconds>` before running a full build.

The on-screen plan excerpts and test results come from the skill's first evaluation run (see the skill's `evals/`). Update them if the skill changes.
