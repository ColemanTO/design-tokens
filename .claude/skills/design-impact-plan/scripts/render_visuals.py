#!/usr/bin/env python3
"""Render an impact plan's two figures as standalone SVGs (light + dark aware).

  python render_visuals.py plan-visuals.json <out-prefix>
    -> <out-prefix>-ladder.svg      Meadows leverage ladder with the trimtabs on their rungs
    -> <out-prefix>-lifecycle.svg   lifecycle strip: impact rating + confidence per stage

Input JSON (see references/visuals.md):
{
  "trimtabs": [{"n": 1, "label": "Poster-first default", "levels": [5, 6]}, ...],
  "lifecycle": {
    "creation":   {"impact": "Low",    "confidence": "High"},
    "delivery":   {"impact": "High",   "confidence": "Medium"},
    "use":        {"impact": "Medium", "confidence": "Medium"},
    "longevity":  {"impact": "High",   "confidence": "Low"},
    "end_of_life":{"impact": "n/a"}
  }
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
  .lowconf{fill:none;stroke-width:2;stroke-dasharray:6 5} .lc-low{stroke:#0b0b0b} .lc-medium,.lc-high{stroke:#ffffff} .lc-key{stroke:#666666}
  @media (prefers-color-scheme: dark){
    .surface{fill:#191919} .ink{fill:#efefef} .ink2{fill:#9c9c9c} .rule{stroke:#303030}
    .axis{stroke:#474747} .hit{fill:#1c2a3d} .mark{fill:#519ced} .marktext{fill:#0b0b0b}
    .r-low{fill:#1757ac} .r-medium{fill:#338ced} .r-high{fill:#9dc8f7} .r-na{fill:#262626}
    .t-low{fill:#ffffff} .t-medium{fill:#0b0b0b} .t-high{fill:#0b0b0b} .t-na{fill:#9c9c9c}
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
    print("\n".join(written) or "nothing to render")


if __name__ == "__main__":
    main()
