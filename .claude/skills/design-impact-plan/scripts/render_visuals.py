#!/usr/bin/env python3
"""Render an impact plan's two figures as standalone SVGs (light + dark aware).

  python render_visuals.py plan-visuals.json <out-prefix>
    -> <out-prefix>-ladder.svg      Meadows leverage ladder with the trimtabs on their rungs
    -> <out-prefix>-lifecycle.svg   lifecycle strip: impact rating + confidence per stage
    -> <out-prefix>-loops.svg       loop map: reinforcing and balancing loops (if "loops" given)

Input JSON (see references/visuals.md):
{
  "trimtabs": [{"n": 1, "label": "Poster-first default", "levels": [5, 6]}, ...],
  "lifecycle": {
    "creation":   {"impact": "Low",    "confidence": "High"},
    "delivery":   {"impact": "High",   "confidence": "Medium"},
    "use":        {"impact": "Medium", "confidence": "Medium"},
    "longevity":  {"impact": "High",   "confidence": "Low"},
    "end_of_life":{"impact": "n/a"}
  },
  "loops": [
    {"id": "R1", "type": "reinforcing", "title": "Cost grows with traffic",
     "steps": ["More visits", "More images generated", "Higher GPU cost and energy"]},
    {"id": "B1", "type": "balancing", "title": "Budget cap", "trimtab": 3, "limits": "R1",
     "steps": ["Spend shown on dashboard", "Budget reached", "Fall back to cached photo"]}
  ]
}
Standard library only. Ratings are qualitative tiers; nothing here invents numbers.
"""
import json
import sys
from html import escape

FONT = "system-ui, -apple-system, 'Segoe UI', Inter, Roboto, sans-serif"

# Chrome + ink (light / dark). Ordinal rating ramp: one hue, validated light->dark
# with the dataviz validator (--ordinal) against #ffffff and #191919 surfaces.
STYLE = """
  .surface{fill:#ffffff} .ink{fill:#191919} .ink2{fill:#666666} .rule{stroke:#e7e7e7}
  .axis{stroke:#c2c2c2} .hit{fill:#eaf2fd} .mark{fill:#2370cd} .marktext{fill:#ffffff}
  .r-low{fill:#84b9f3} .r-medium{fill:#257de0} .r-high{fill:#0f4a96} .r-na{fill:#f1f1f1}
  .t-low{fill:#0b0b0b} .t-medium{fill:#ffffff} .t-high{fill:#ffffff} .t-na{fill:#666666}
  .lp-b{stroke:#257de0} .lp-r{stroke:#f47230} .lf-b{fill:#257de0} .lf-r{fill:#f47230} .lt-b{fill:#ffffff} .lt-r{fill:#0b0b0b}
  .box{fill:#f6f6f6} .tag{fill:#eaf2fd}
  .lowconf{fill:none;stroke-width:2;stroke-dasharray:6 5} .lc-low{stroke:#0b0b0b} .lc-medium,.lc-high{stroke:#ffffff} .lc-key{stroke:#666666}
  @media (prefers-color-scheme: dark){
    .surface{fill:#191919} .ink{fill:#efefef} .ink2{fill:#9c9c9c} .rule{stroke:#303030}
    .axis{stroke:#474747} .hit{fill:#1c2a3d} .mark{fill:#519ced} .marktext{fill:#0b0b0b}
    .r-low{fill:#1757ac} .r-medium{fill:#338ced} .r-high{fill:#9dc8f7} .r-na{fill:#262626}
    .t-low{fill:#ffffff} .t-medium{fill:#0b0b0b} .t-high{fill:#0b0b0b} .t-na{fill:#9c9c9c}
    .lp-b{stroke:#338ced} .lp-r{stroke:#e76624} .lf-b{fill:#338ced} .lf-r{fill:#e76624} .lt-b{fill:#0b0b0b} .lt-r{fill:#0b0b0b}
    .box{fill:#232323} .tag{fill:#1c2a3d}
    .lc-low{stroke:#ffffff} .lc-medium,.lc-high{stroke:#0b0b0b} .lc-key{stroke:#9c9c9c}
  }
"""

LEVELS = {
    1: "Power to transcend paradigms",
    2: "Mindset or paradigm",
    3: "Goals of the system",
    4: "Self-organization",
    5: "Rules and defaults",
    6: "Information flows",
    7: "Reinforcing loops",
    8: "Balancing loops",
    9: "Delays",
    10: "Material stocks and flows",
    11: "Buffers",
    12: "Parameters and numbers",
}

STAGES = [("creation", "Creation"), ("delivery", "Delivery"), ("use", "Use"),
          ("longevity", "Longevity"), ("end_of_life", "End of life")]


def svg(width, height, title, desc, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d" font-family="{FONT}">\n'
            f'<title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>\n'
            f'<style>{STYLE}</style>\n'
            f'<rect class="surface" width="{width}" height="{height}" rx="12"/>\n{body}</svg>\n')


def trunc(s, n):
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def ladder(trimtabs):
    W, top, row, left = 760, 78, 38, 64
    by_level = {lvl: [] for lvl in LEVELS}
    for t in trimtabs:
        levels = t.get("levels") or []
        for i, lvl in enumerate(levels):
            if lvl in by_level:
                by_level[lvl].append((t, i == 0))
    out = [f'<text class="ink" x="24" y="34" font-size="20" font-weight="600">Where the trimtabs sit on Meadows’ ladder</text>',
           f'<text class="ink2" x="24" y="56" font-size="13">Leverage points, strongest at the top. Numbered markers are this plan’s trimtabs.</text>']
    # stronger/weaker axis
    y0, y1 = top + 6, top + 12 * row - 6
    out.append(f'<line class="axis" x1="34" y1="{y1}" x2="34" y2="{y0 + 10}" stroke-width="2"/>')
    out.append(f'<path class="ink2" d="M28 {y0 + 14} L34 {y0 + 2} L40 {y0 + 14} Z"/>')
    out.append(f'<text class="ink2" font-size="11" transform="translate(22 {y0 + 92}) rotate(-90)" text-anchor="middle">STRONGER</text>')
    out.append(f'<text class="ink2" font-size="11" transform="translate(22 {y1 - 40}) rotate(-90)" text-anchor="middle">WEAKER</text>')
    for k, lvl in enumerate(range(1, 13)):
        y = top + k * row
        cy = y + row / 2
        hits = by_level[lvl]
        if hits:
            out.append(f'<rect class="hit" x="{left - 8}" y="{y + 3}" width="{W - left - 16}" height="{row - 6}" rx="8"/>')
        out.append(f'<line class="rule" x1="{left}" y1="{y + row}" x2="{W - 24}" y2="{y + row}" stroke-width="1"/>')
        weight = "600" if hits else "400"
        cls = "ink" if hits else "ink2"
        out.append(f'<text class="{cls}" x="{left}" y="{cy + 5}" font-size="14" font-weight="{weight}">'
                   f'<tspan font-variant-numeric="tabular-nums">{lvl:>2}</tspan>  {escape(LEVELS[lvl])}</text>')
        x = 300
        for t, primary in hits:
            out.append(f'<g><title>Trimtab {t["n"]}: {escape(t["label"])} (level {lvl})</title>'
                       f'<circle class="mark" cx="{x}" cy="{cy}" r="12"/>'
                       f'<text class="marktext" x="{x}" y="{cy + 5}" font-size="13" font-weight="700" text-anchor="middle">{t["n"]}</text></g>')
            x += 30
    # key: full trimtab text, so nothing on the rungs is truncated
    ky = top + 12 * row + 30
    for t in trimtabs:
        lv = " + ".join(f'{l} {LEVELS.get(l, "")}'.strip() for l in t.get("levels", []))
        out.append(f'<circle class="mark" cx="{left + 4}" cy="{ky - 5}" r="10"/>'
                   f'<text class="marktext" x="{left + 4}" y="{ky}" font-size="12" font-weight="700" text-anchor="middle">{t["n"]}</text>')
        out.append(f'<text class="ink" x="{left + 24}" y="{ky}" font-size="14">{escape(trunc(t["label"], 70))}</text>')
        out.append(f'<text class="ink2" x="{left + 24}" y="{ky + 18}" font-size="12">Level {escape(lv)}</text>')
        ky += 46
    H = ky - 6
    placed = ", ".join(f'#{t["n"]} {t["label"]} (level {"/".join(map(str, t.get("levels", [])))})' for t in trimtabs)
    return svg(W, H, "Trimtabs on Meadows' leverage ladder",
               f"Twelve leverage points, strongest at the top. Trimtabs: {placed}.", "\n".join(out))


def lifecycle(stages):
    W, gap, x0, y0, h = 760, 8, 24, 74, 132
    cw = (W - 2 * x0 - 4 * gap) / 5
    out = [f'<text class="ink" x="24" y="34" font-size="20" font-weight="600">Where the impact sits</text>',
           f'<text class="ink2" x="24" y="56" font-size="13">Impact rating per lifecycle stage, relative to the rest of this design. Not a measurement.</text>']
    summary = []
    for i, (key, name) in enumerate(STAGES):
        s = stages.get(key, {}) or {}
        impact = str(s.get("impact", "n/a")).strip()
        conf = str(s.get("confidence", "")).strip()
        tier = impact.lower() if impact.lower() in ("low", "medium", "high") else "na"
        x = x0 + i * (cw + gap)
        out.append(f'<g><title>{name}: impact {impact}{", confidence " + conf if conf else ""}</title>')
        out.append(f'<rect class="r-{tier}" x="{x:.1f}" y="{y0}" width="{cw:.1f}" height="{h}" rx="10"/>')
        if tier != "na" and conf.lower() == "low":
            out.append(f'<rect class="lowconf lc-{tier}" x="{x + 4:.1f}" y="{y0 + 4}" width="{cw - 8:.1f}" height="{h - 8}" rx="7"/>')
        tx = x + 16
        out.append(f'<text class="t-{tier}" x="{tx:.1f}" y="{y0 + 30}" font-size="12" font-weight="600" letter-spacing=".06em">{name.upper()}</text>')
        out.append(f'<text class="t-{tier}" x="{tx:.1f}" y="{y0 + 72}" font-size="26" font-weight="700">{escape("n/a" if tier == "na" else impact.capitalize())}</text>')
        if conf and tier != "na":
            out.append(f'<text class="t-{tier}" x="{tx:.1f}" y="{y0 + 104}" font-size="12">{escape(conf.lower())} confidence</text>')
        out.append('</g>')
        summary.append(f"{name} {impact}" + (f" ({conf.lower()} confidence)" if conf and tier != "na" else ""))
    # legend
    ly = y0 + h + 34
    lx = 24
    for tier, label in (("low", "Low"), ("medium", "Medium"), ("high", "High")):
        out.append(f'<rect class="r-{tier}" x="{lx}" y="{ly - 12}" width="16" height="16" rx="4"/>')
        out.append(f'<text class="ink2" x="{lx + 22}" y="{ly + 1}" font-size="13">{label}</text>')
        lx += 92
    out.append(f'<rect class="lowconf lc-key" x="{lx + 8}" y="{ly - 12}" width="16" height="16" rx="4" style="stroke-width:1.5;stroke-dasharray:3 2"/>')
    out.append(f'<text class="ink2" x="{lx + 30}" y="{ly + 1}" font-size="13">Dashed outline = low confidence: find out before deciding</text>')
    H = ly + 22
    return svg(W, H, "Impact by lifecycle stage", "Impact rating per stage: " + "; ".join(summary) + ".", "\n".join(out))


def wrap(text, width_px, size):
    """Greedy word wrap using an average glyph width; good enough for short labels."""
    per_line = max(6, int(width_px / (size * 0.56)))
    lines, cur = [], ""
    for w in text.split():
        if cur and len(cur) + 1 + len(w) > per_line:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    if len(lines) > 3:
        lines = lines[:3]
        lines[-1] = trunc(lines[-1] + "…", per_line)
    return lines


def loops_map(loops):
    W, x0, right, gap = 760, 24, 64, 26
    loops = loops[:3]
    out = [f'<text class="ink" x="24" y="34" font-size="20" font-weight="600">How the system behaves</text>',
           f'<text class="ink2" x="24" y="56" font-size="13">Feedback loops this design creates (R, reinforcing) and the ones that hold them in check (B, balancing).</text>']
    y = 84
    rows = {}
    summary = []
    for lp in loops:
        kind = "r" if str(lp.get("type", "")).lower().startswith("r") else "b"
        kind_name = "Reinforcing" if kind == "r" else "Balancing"
        lid = escape(str(lp.get("id", kind.upper())))
        steps = [str(x) for x in lp.get("steps", [])][:5] or ["(no steps given)"]
        # header: badge + type + title (+ trimtab tag)
        out.append(f'<rect class="lf-{kind}" x="{x0}" y="{y}" width="34" height="24" rx="6"/>'
                   f'<text class="lt-{kind}" x="{x0 + 17}" y="{y + 17}" font-size="13" font-weight="700" text-anchor="middle">{lid}</text>')
        out.append(f'<text class="ink" x="{x0 + 44}" y="{y + 17}" font-size="15" font-weight="600">{escape(trunc(str(lp.get("title", "")), 60))}'
                   f'<tspan class="ink2" font-weight="400" font-size="13">  ·  {kind_name}</tspan></text>')
        if lp.get("trimtab"):
            tx = W - right - 128
            out.append(f'<rect class="tag" x="{tx}" y="{y}" width="128" height="24" rx="12"/>'
                       f'<circle class="mark" cx="{tx + 14}" cy="{y + 12}" r="9"/>'
                       f'<text class="marktext" x="{tx + 14}" y="{y + 16}" font-size="11" font-weight="700" text-anchor="middle">{int(lp["trimtab"])}</text>'
                       f'<text class="ink" x="{tx + 30}" y="{y + 16}" font-size="12">from trimtab</text>')
        # step boxes
        by = y + 38
        n = len(steps)
        arrow = 22
        bw = (W - x0 - right - (n - 1) * arrow) / n
        lines_per = [wrap(st, bw - 16, 13) for st in steps]
        bh = 20 + 17 * max(len(l) for l in lines_per)
        for i, (st, lines) in enumerate(zip(steps, lines_per)):
            bx = x0 + i * (bw + arrow)
            out.append(f'<rect class="box lp-{kind}" x="{bx:.1f}" y="{by}" width="{bw:.1f}" height="{bh}" rx="10" stroke-width="2"/>')
            ty = by + bh / 2 - (len(lines) - 1) * 17 / 2 + 5
            for j, ln in enumerate(lines):
                out.append(f'<text class="ink" x="{bx + bw / 2:.1f}" y="{ty + j * 17:.1f}" font-size="13" text-anchor="middle">{escape(ln)}</text>')
            if i < n - 1:
                ax = bx + bw + 3
                ay = by + bh / 2
                out.append(f'<path class="lp-{kind}" d="M{ax:.1f} {ay} H{ax + arrow - 8:.1f}" stroke-width="2" fill="none"/>'
                           f'<path class="lf-{kind}" d="M{ax + arrow - 9:.1f} {ay - 5} L{ax + arrow - 3:.1f} {ay} L{ax + arrow - 9:.1f} {ay + 5} Z"/>')
        # return path closing the loop: last box bottom -> down -> left -> up into first box
        first_cx = x0 + bw / 2
        last_cx = x0 + (n - 1) * (bw + arrow) + bw / 2
        yb = by + bh
        yr = yb + 22
        if n > 1:
            out.append(f'<path class="lp-{kind}" d="M{last_cx:.1f} {yb} V{yr - 8} Q{last_cx:.1f} {yr} {last_cx - 8:.1f} {yr} H{first_cx + 8:.1f} '
                       f'Q{first_cx:.1f} {yr} {first_cx:.1f} {yr - 8} V{yb + 9}" stroke-width="2" fill="none"/>'
                       f'<path class="lf-{kind}" d="M{first_cx - 5:.1f} {yb + 10} L{first_cx:.1f} {yb + 3} L{first_cx + 5:.1f} {yb + 10} Z"/>')
            out.append(f'<text class="ink2" x="{(first_cx + last_cx) / 2:.1f}" y="{yr - 6}" font-size="12" text-anchor="middle">'
                       f'{"and round again, faster" if kind == "r" else "and back toward the limit"}</text>')
        rows[str(lp.get("id"))] = (by + bh / 2, kind)
        summary.append(f'{lp.get("id")} {kind_name.lower()} "{lp.get("title", "")}": ' + " → ".join(steps))
        y = yr + 30
    # limits connectors on the right margin
    cx = W - right + 30
    for lp in loops:
        tgt = str(lp.get("limits", ""))
        if tgt and tgt in rows and str(lp.get("id")) in rows:
            ya, kind = rows[str(lp.get("id"))]
            yb_, _ = rows[tgt]
            out.append(f'<path class="lp-b" d="M{W - right + 4} {ya} H{cx} V{yb_} H{W - right + 10}" stroke-width="2" fill="none" stroke-dasharray="5 4"/>'
                       f'<path class="lf-b" d="M{W - right + 12} {yb_ - 5} L{W - right + 5} {yb_} L{W - right + 12} {yb_ + 5} Z"/>')
            out.append(f'<text class="ink2" font-size="12" transform="translate({cx + 14} {(ya + yb_) / 2}) rotate(-90)" text-anchor="middle">limits {escape(tgt)}</text>')
            summary.append(f'{lp.get("id")} limits {tgt}')
    H = y - 8
    return svg(W, H, "Feedback loops", "Loop map. " + "; ".join(summary) + ".", "\n".join(out))


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    data = json.load(open(sys.argv[1]))
    prefix = sys.argv[2]
    written = []
    if data.get("trimtabs"):
        open(f"{prefix}-ladder.svg", "w").write(ladder(data["trimtabs"]))
        written.append(f"{prefix}-ladder.svg")
    if data.get("lifecycle"):
        open(f"{prefix}-lifecycle.svg", "w").write(lifecycle(data["lifecycle"]))
        written.append(f"{prefix}-lifecycle.svg")
    if data.get("loops"):
        open(f"{prefix}-loops.svg", "w").write(loops_map(data["loops"]))
        written.append(f"{prefix}-loops.svg")
    print("\n".join(written) or "nothing to render")


if __name__ == "__main__":
    main()
