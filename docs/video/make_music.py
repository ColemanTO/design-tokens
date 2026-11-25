"""Synthesize an original ambient music bed: pads + plucked arpeggio + soft low pulse.
Usage: python make_music.py <duration_seconds> <out.wav>
"""
import sys
import numpy as np
import soundfile as sf

SR = 48000
dur = float(sys.argv[1])
out = sys.argv[2]
N = int(SR * dur)
t = np.arange(N) / SR
rng = np.random.default_rng(7)

BPM = 72
beat = 60 / BPM
bar = beat * 4
chord_len = bar * 2  # two bars per chord


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


# D major, gentle and hopeful: Dmaj9, Bm7(add11), Gmaj7, Asus2/E-ish
progression = [
    [50, 57, 61, 64, 66],  # D A C# E F#
    [47, 54, 57, 62, 64],  # B F# A D E
    [43, 50, 54, 59, 62],  # G D F# B D
    [45, 52, 57, 59, 64],  # A E A B E
]


def one_pole_lp(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    # vectorised via lfilter-like recursion in chunks would be faster; keep simple but OK for ~2-3 min
    for i in range(len(x)):
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def saw(freq, tt, phase=0.0):
    return 2 * ((freq * tt + phase) % 1.0) - 1


pad = np.zeros(N)
pulse = np.zeros(N)
arp = np.zeros(N)

n_chords = int(np.ceil(dur / chord_len)) + 1
for c in range(n_chords):
    start = c * chord_len
    s0 = int(start * SR)
    if s0 >= N:
        break
    length = int((chord_len + 1.5) * SR)  # overlap for smooth crossfade
    s1 = min(N, s0 + length)
    tt = np.arange(s1 - s0) / SR
    chord = progression[c % len(progression)]
    env = np.minimum(1, tt / 1.8) * np.clip((chord_len + 1.5 - tt) / 1.8, 0, 1)
    seg = np.zeros(s1 - s0)
    for n in chord[1:]:
        f = midi(n)
        for det in (-0.08, 0.0, 0.08):  # detuned triplet for warmth
            seg += saw(f * 2 ** (det / 12), tt, rng.random()) * 0.06
    pad[s0:s1] += seg * env
    # low root pulse on each beat, soft sine
    root = midi(chord[0] - 12)
    for b in range(8):
        bs = s0 + int(b * beat * SR)
        if bs >= N:
            break
        L = min(N - bs, int(beat * SR))
        bt = np.arange(L) / SR
        pulse[bs:bs + L] += np.sin(2 * np.pi * root * bt) * np.exp(-bt * 3.0) * (0.22 if b % 4 == 0 else 0.12)
    # plucked arpeggio in eighth notes, an octave up, sparse pattern
    pattern = [1, 2, 3, 4, 3, 2, 4, 3]
    for k in range(16):
        if k % 8 in (5,):  # leave breathing gaps
            continue
        ns = s0 + int(k * beat / 2 * SR)
        if ns >= N:
            break
        L = min(N - ns, int(1.6 * SR))
        nt = np.arange(L) / SR
        f = midi(chord[pattern[k % 8]] + 12)
        tone = np.sin(2 * np.pi * f * nt) + 0.3 * np.sin(2 * np.pi * 2 * f * nt) * np.exp(-nt * 6)
        arp[ns:ns + L] += tone * np.exp(-nt * 2.8) * 0.07

pad = one_pole_lp(pad, 1400)

# simple stereo reverb: convolve with decaying noise impulse responses
def reverb(x, seconds=2.6, seed=1):
    r = np.random.default_rng(seed)
    L = int(seconds * SR)
    ir = r.standard_normal(L) * np.exp(-np.arange(L) / SR * 3.2)
    ir /= np.sqrt(np.sum(ir ** 2))
    n = len(x) + L
    nfft = 1 << (n - 1).bit_length()
    y = np.fft.irfft(np.fft.rfft(x, nfft) * np.fft.rfft(ir, nfft), nfft)[: len(x)]
    return y

dry = pad + pulse + arp
left = 0.75 * dry + 0.45 * reverb(pad + arp, seed=1)
right = 0.75 * dry + 0.45 * reverb(pad + arp, seed=2)
# gentle stereo movement on the arpeggio
pan = 0.5 + 0.25 * np.sin(2 * np.pi * t / 9)
left += arp * 0.3 * (1 - pan)
right += arp * 0.3 * pan

stereo = np.stack([left, right], axis=1)
fade_in = np.minimum(1, t / 3.0)
fade_out = np.clip((dur - t) / 5.0, 0, 1)
stereo *= (fade_in * fade_out)[:, None]
stereo /= np.max(np.abs(stereo)) + 1e-9
stereo *= 0.89
sf.write(out, stereo.astype(np.float32), SR)
print(f"wrote {out} ({dur:.1f}s)")
