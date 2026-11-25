# Plan templates

There are two formats. **The one-page brief is the default.** Write the full plan only when someone asks for it (see "When to write the full plan" below).

Both are written for a collaborator who wasn't in the conversation. Drop any section with nothing real to say; never pad.

## Contents
- One-page brief (default)
- Full plan
- When to write the full plan
- Notes on the fields

## One-page brief (default)

**Budget: 650–700 words of text**, not counting figure alt text. That's what fits on one page and gets read; don't go over 700. The analysis behind it is just as thorough as for the full plan: run every lens, then keep only what changes a decision. If you're over budget, cut detail from the findings and assumptions, never the verdict or the trimtabs.

```markdown
# Impact brief: <design name>

<date> · <author / team> · Status: draft · *One-page brief; a full plan is available on request.*

## Verdict: <Build | Build differently | Reconsider | Don't build>
<One or two sentences: why, in plain language. For Reconsider / Don't build, name the smaller alternative.>

## The trimtabs
1. **<Change>.** <One or two sentences: what it reduces and why it's high leverage.> *Leverage: <Meadows level, e.g. rules / defaults (5)>. Effort: <low/med/high>.*
2. ...
3. ...

![Leverage ladder: <which trimtabs sit on which rungs>](<slug>-ladder.svg)

## Decide first
- **<Decision>:** <recommended choice and why it can't wait, in one line>.
- (at most three)

## Where the impact sits
![Lifecycle strip: <stage> <tier>, ... (<stage> low confidence)](<slug>-lifecycle.svg)

- **<Finding>.** <One line.> *(<Impact> impact, <confidence> confidence)*
- (at most four: the ones that drive the verdict, plus any low-confidence High that needs checking)

## Watch for
- <People or systems that bear the cost, a trade-off the team must decide, or an accessibility constraint. One line each, at most three.>

## How we'll know
- <Measure the team can actually collect, one line each, at most three.>

## Assumptions
- <Assumption or open question that could change the verdict. At most four.>

---
*Lenses: Norman (Design for a Better World), Fuller (Critical Path), Meadows (Thinking in Systems).*
```

Design-token changes go into a trimtab when they are one; otherwise, mention the most important one in a single line under "Decide first" or "Watch for".

## Full plan

The complete version, for when the brief isn't enough. Aim for two to four pages.

```markdown
# Impact plan: <design name>

<date> · <author / team> · Status: draft

## Verdict: <Build | Build differently | Reconsider | Don't build>
<One or two sentences: why, in plain language.>

## The trimtabs
The few changes with the most leverage, in priority order.
1. **<Change>** — <what it reduces and why it's high leverage>. <Leverage: Meadows level, e.g. "rules / defaults (5)">. <Effort: low/med/high.>
2. ...

![Leverage ladder: <which trimtabs sit on which rungs>](<slug>-ladder.svg)

## What we're designing
<The job it does, for whom, at what scale and lifespan. Is it solving the root problem? Note anything already decided vs. still open.>

## Critical path
Decisions that gate everything downstream and are hard to reverse — make these first.
- **<Decision>** — <options, recommended choice, why it matters now>.

## Findings
![Lifecycle strip: <stage> <tier>, ... (<stage> low confidence)](<slug>-lifecycle.svg)

| Area | Finding | Impact | Confidence | Recommendation |
|------|---------|--------|------------|----------------|
| <Lifecycle stage / Behavior / System> | <specific to this design> | High/Med/Low | High/Med/Low | <specific change> |

## People and systems affected
<Who bears costs outside the project: other communities, staff, people on older devices, suppliers, waste streams. Who could help shape it?>

## Trade-offs
<Where sustainability competes with other goals, and how it was resolved or what is left for the team to decide. Accessibility is a fixed constraint, not a trade-off.>

## Design token changes
<Only if relevant. Token/group → change → findings it addresses.>

## How we'll know
<2–4 measures the team can actually collect, with a baseline if possible. Name the method if any numbers are estimated.>

## Assumptions and open questions
- <Assumption made because information was missing>
- <Question for the team>

---
*Lenses: Norman's humanity-centered design (Design for a Better World); Fuller's comprehensive anticipatory design science (Critical Path); Meadows' leverage points (Thinking in Systems).*

## Changelog
- <date> — created
```

## When to write the full plan

Write the full plan instead of the brief when the user asks for it ("full plan", "detailed", "everything"), or when the plan is going to a formal review, a client deliverable, or a compliance or procurement process that needs the reasoning on record. When the user asks to expand a brief, replace the brief in the same file with the full plan; don't keep two versions.

After a brief, offer the full plan in one line rather than writing it unasked.

## Notes on the fields
- **Impact** is the size of the effect relative to the rest of this design, not an absolute figure.
- **Confidence** is how sure you are given the information available. Low confidence plus high impact means "find out before deciding" — say what to find out.
- Put any numbers in the findings only with their source method and inputs.
