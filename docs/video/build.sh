#!/usr/bin/env bash
# Build the Design Impact Plan overview video from source.
# Requires: python3, ffmpeg, node with Playwright + Chromium.
# Usage: ./build.sh [voice]   (default voice: af_heart)
set -euo pipefail
cd "$(dirname "$0")"
VOICE="${1:-af_heart}"
MODELS_URL="https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0"

# 1. Python environment and Kokoro model files
if [ ! -d venv ]; then
  python3 -m venv venv
  ./venv/bin/pip install -q -r requirements.txt
fi
mkdir -p models
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -f "models/$f" ] || curl -sSL -o "models/$f" "$MODELS_URL/$f"
done

# 2. Narration (one clip per scene) -> vo.wav + timings.json
./venv/bin/python make_vo.py "$VOICE"
TOTAL=$(./venv/bin/python -c "import json; print(json.load(open('timings.json'))['total'])")

# 3. Original music bed, exactly as long as the narration
./venv/bin/python make_music.py "$TOTAL" music.wav

# 4. Mix: compressed voice, music ducked under it, normalized to -16 LUFS
ffmpeg -y -loglevel error -i vo.wav -i music.wav -filter_complex \
  "[0:a]aresample=48000,aformat=channel_layouts=stereo,highpass=f=70,acompressor=threshold=-20dB:ratio=3:attack=5:release=80:makeup=2,asplit=2[vo][sc];\
[1:a]volume=0.30[mus];[mus][sc]sidechaincompress=threshold=0.02:ratio=8:attack=60:release=700[duck];\
[vo][duck]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[out]" \
  -map "[out]" -c:a pcm_s16le mix.wav

# 5. Frame-by-frame capture of scenes.html, timed to the narration
node capture.js video-silent.mp4 30

# 6. Mux video + audio
ffmpeg -y -loglevel error -i video-silent.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy \
  -c:a aac -b:a 192k -ac 2 -disposition:a:0 default -movflags +faststart -shortest \
  design-impact-plan-overview.mp4
ffmpeg -y -loglevel error -i mix.wav -c:a libmp3lame -b:a 192k design-impact-plan-soundtrack.mp3

echo "Built design-impact-plan-overview.mp4 (${TOTAL}s)"
