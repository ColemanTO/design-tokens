# Plan figures: the leverage ladder and the lifecycle strip

Two small figures make a plan readable at a glance. They show structure and ratings, never measurements, so they keep the skill's honesty rules: no invented numbers, and every color also has a text label.

- **Leverage ladder:** Meadows' twelve leverage points, strongest at the top, with each trimtab's numbered marker on its rung and a key below. A reader can see straight away whether the plan reaches for rules and goals or stops at parameter tweaks.
- **Lifecycle strip:** five cells (creation → delivery → use → longevity → end of life), each showing the stage's impact tier and how confident the rating is. It shows where the impact concentrates.

## Rendering

`scripts/render_visuals.py` turns a small JSON summary into two SVGs. It uses only the Python standard library. The SVGs follow the viewer's light or dark preference, and each has a title and description for screen readers.

```bash
python <skill-dir>/scripts/render_visuals.py <plan-slug>-visuals.json impact-plans/<plan-slug>
# -> impact-plans/<plan-slug>-ladder.svg and impact-plans/<plan-slug>-lifecycle.svg
```

Write the JSON from the finished plan, so the figures match the text exactly:

```json
{
  "trimtabs": [
    {"n": 1, "label": "Poster-first default; video only when cheap and welcome", "levels": [5]},
    {"n": 2, "label": "Video stops by itself, with a pause control", "levels": [8]},
    {"n": 3, "label": "No-autoplay rule with a token mode and CI weight budget", "levels": [5, 6]}
  ],
  "lifecycle": {
    "creation":    {"impact": "Medium", "confidence": "Medium"},
    "delivery":    {"impact": "High",   "confidence": "High"},
    "use":         {"impact": "Medium", "confidence": "Medium"},
    "longevity":   {"impact": "High",   "confidence": "Low"},
    "end_of_life": {"impact": "Low",    "confidence": "Medium"}
  }
}
```

Rules for filling it in:
- **Trimtab labels** are a short version of the trimtab's bold heading, under about 70 characters. `levels` lists Meadows levels (1–12), primary level first. A trimtab that works at two levels gets a marker on each rung.
- **One tier per stage:** `Low`, `Medium` or `High`. If a stage has several findings, use the highest, with that finding's confidence. Don't write ranges like "Med–High" in the JSON: pick the tier you'd defend. The plan's findings table can still hold the nuance.
- **`n/a`** for a stage that genuinely doesn't apply (e.g. no physical end of life for a short-lived campaign page). Use it sparingly, because almost every design has some impact at every stage.
- **Confidence** is `Low`, `Medium` or `High`. Low confidence gets a dashed outline, which tells the reader to find out before deciding.
- Keep the JSON next to the plan (`impact-plans/<plan-slug>-visuals.json`) so the figures can be re-rendered when the plan changes.

## Placing them in the plan

Embed the ladder right after **The trimtabs**, and the strip at the top of **Where the impact sits** (brief) or **Findings** (full plan), with descriptive alt text:

```markdown
![Leverage ladder: trimtabs 1 and 3 at rules and defaults (5), 3 also at information flows (6), 2 at balancing loops (8)](homepage-hero-ladder.svg)
```

The figures supplement the text; they don't replace it. The trimtab list and the findings stay in the plan, so screen-reader users and anyone reading plain text get the same information.

If the plan is only being shown in chat (no files saved), skip the figures, or offer to save the plan with them.
