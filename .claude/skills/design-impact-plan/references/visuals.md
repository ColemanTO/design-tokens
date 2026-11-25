# Plan figures: leverage ladder, lifecycle strip, loop map

Three small figures make a plan readable at a glance. They show structure and ratings, never measurements, so they keep the skill's honesty rules: no invented numbers, and every color also has a text label.

- **Leverage ladder:** Meadows' twelve leverage points, strongest at the top, with each trimtab's numbered marker on its rung and a key below. A reader can see straight away whether the plan reaches for rules and goals or stops at parameter tweaks.
- **Lifecycle strip:** five cells (creation → delivery → use → longevity → end of life), each showing the stage's impact tier and how confident the rating is. It shows where the impact concentrates.
- **Loop map** (optional): the feedback loops the behavior lens found, drawn the way Meadows drew systems. Reinforcing loops (R) amplify use or cost; balancing loops (B) hold them in check. It explains *why* a trimtab works. Include it only when the plan names at least one real loop.

## Rendering

`scripts/render_visuals.py` turns a small JSON summary into the SVGs (the loop map only if `loops` is present). It uses only the Python standard library. The SVGs follow the viewer's light or dark preference, and each has a title and description for screen readers.

```bash
python <skill-dir>/scripts/render_visuals.py <plan-slug>-visuals.json impact-plans/<plan-slug>
# -> impact-plans/<plan-slug>-ladder.svg, -lifecycle.svg, and -loops.svg if loops are given
```

Write the JSON from the finished plan, so the figures match the text exactly. This example is from an unrelated design (a fitness app's streak reminders); find the loops in the design in front of you, don't reuse these:

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
  },
  "loops": [
    {"id": "R1", "type": "reinforcing", "title": "Streaks breed more nudges",
     "steps": ["Streak reminders lift daily opens", "Team adds more reminder types", "More notifications and wake-ups"]},
    {"id": "B1", "type": "balancing", "title": "Weekly notification cap", "trimtab": 2, "limits": "R1",
     "steps": ["Sends per user tracked against a cap", "Cap reached", "Lower-value reminders dropped"]}
  ]
}
```

Rules for filling it in:
- **Trimtab labels** are a short version of the trimtab's bold heading, under about 70 characters. `levels` lists Meadows levels (1–12), primary level first. A trimtab that works at two levels gets a marker on each rung.
- **One tier per stage:** `Low`, `Medium` or `High`. If a stage has several findings, use the highest, with that finding's confidence. Don't write ranges like "Med–High" in the JSON: pick the tier you'd defend. The plan's findings table can still hold the nuance.
- **`n/a`** for a stage that genuinely doesn't apply (e.g. no physical end of life for a short-lived campaign page). Use it sparingly, because almost every design has some impact at every stage.
- **Confidence** is `Low`, `Medium` or `High`. Low confidence gets a dashed outline, which tells the reader to find out before deciding.
- **Loops** (optional, at most three): `type` is `reinforcing` or `balancing`; `steps` are 2–5 short causal steps (under ~45 characters each) where the last step feeds back into the first. Check that it really closes: a reinforcing loop amplifies itself on each pass; a balancing loop pushes back toward a limit. A list of steps that doesn't feed back isn't a loop: a chain of consequences (image drifts → wrong product arrives → returns) belongs in the findings, not on the loop map. Set `trimtab` when the loop is the mechanism a trimtab adds, and `limits` to the ID of the reinforcing loop a balancing loop holds in check.
- Keep the JSON next to the plan (`impact-plans/<plan-slug>-visuals.json`) so the figures can be re-rendered when the plan changes.

## Placing them in the plan

Embed the ladder right after **The trimtabs**, followed by the loop map if there is one, and the strip at the top of **Where the impact sits** (brief) or **Findings** (full plan), with descriptive alt text:

```markdown
![Leverage ladder: trimtabs 1 and 3 at rules and defaults (5), 3 also at information flows (6), 2 at balancing loops (8)](homepage-hero-ladder.svg)
```

The figures supplement the text; they don't replace it. The trimtab list and the findings stay in the plan, so screen-reader users and anyone reading plain text get the same information.

If the plan is only being shown in chat (no files saved), skip the figures, or offer to save the plan with them.
