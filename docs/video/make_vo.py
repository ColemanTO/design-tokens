"""Generate per-scene voiceover with Kokoro and write timings.json.
Usage: python make_vo.py <voice>
"""
import json, sys
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

voice = sys.argv[1] if len(sys.argv) > 1 else "af_heart"
k = Kokoro("models/kokoro-v1.0.onnx", "models/voices-v1.0.bin")
scenes = json.load(open("script.json"))
LEAD, GAP = 1.0, 1.1  # seconds of silence before first line / between scenes
SR = 24000
parts, timings, cursor = [np.zeros(int(LEAD * SR))], [], LEAD
for s in scenes:
    audio, sr = k.create(s["vo"], voice=voice, speed=0.98, lang="en-us")
    assert sr == SR
    d = len(audio) / SR
    timings.append({"id": s["id"], "start": round(cursor - (LEAD if not timings else GAP / 2), 3), "vo_start": round(cursor, 3), "vo_end": round(cursor + d, 3)})
    parts += [audio, np.zeros(int(GAP * SR))]
    cursor += d + GAP
tail = 2.5
parts.append(np.zeros(int(tail * SR)))
total = cursor + tail
for i, tm in enumerate(timings):
    tm["end"] = timings[i + 1]["start"] if i + 1 < len(timings) else round(total, 3)
timings[0]["start"] = 0.0
sf.write("vo.wav", np.concatenate(parts).astype(np.float32), SR)
json.dump({"total": round(total, 3), "scenes": timings}, open("timings.json", "w"), indent=2)
print(json.dumps({"total": round(total, 1), "scenes": [(t["id"], round(t["end"] - t["start"], 1)) for t in timings]}))
