---
name: design-impact-plan
description: Plan the environmental and societal impact of a new design before it is built — digital products, features, screens, design systems, and "phygital" work (kiosks, connected/IoT products, smart packaging, QR/AR, retail and event installations). Produces a shareable impact plan with a clear verdict (build / build differently / reconsider / don't build), ranked leverage points, lifecycle and behavioral findings, and concrete design and design-token changes. Grounded in Don Norman, Buckminster Fuller and Donella Meadows. Use this whenever someone is starting or reviewing a new design, feature, product, campaign, or physical-digital experience and mentions sustainability, carbon, energy, e-waste, footprint, eco-design, green UX, longevity, repairability, planned obsolescence, "doing more with less", leverage points, Norman, Fuller, or Meadows — and also when they ask "should we build this?" or want a pre-mortem on unintended consequences, even if they never say "environment".
---

# Design Impact Plan

Help a designer think through what a new design will cost the world — energy, materials, devices, attention, communities — *while the decisions are still cheap to change*, and leave them with a short plan they can act on and share with collaborators.

## The stance (why this skill exists)

Three thinkers shape how this skill works. Read `references/frameworks.md` when you want the fuller version or need to explain a lens to the user.

- **Don Norman, *Design for a Better World*:** we optimize what we measure, and we measure the wrong things. Humanity-centered design looks past the individual user to the whole ecosystem, the long term, and the communities affected; it favors solving root problems, small modular steps that can be tested and corrected, and designing *with* people rather than for them. Repair, reuse, and circularity beat disposability.
- **Buckminster Fuller, *Critical Path*:** be a comprehensive, *anticipatory* designer — think about the whole system before you act on a part. There is no "away" on Spaceship Earth. Ephemeralization — doing ever more with ever less — is the direction of good design. Look for the **trimtab**: the small, well-placed change that turns the whole ship. And sequence the work: some decisions gate everything after them.
- **Donella Meadows, *Thinking in Systems* and "Leverage Points":** systems are stocks, flows, feedback loops and delays, and the places to intervene are not equal. Changing a number (a parameter) is the weakest lever; changing information flows, rules, goals or mindset is far stronger. Use her ladder to rank trimtabs, and watch for levers pulled in the wrong direction.

In practice this means:

1. **Anticipate, don't audit.** The most valuable output is changing a decision before it's made. Lead with the decisions that are still open and expensive to reverse later.
2. **Honest over impressive.** Never invent numbers. Use qualitative tiers (High / Medium / Low) with a stated confidence and the reasoning. Give a figure only if it comes from a named methodology the user can check (e.g., Sustainable Web Design model, CO2.js, a manufacturer LCA) or from data the user supplied — and show the inputs. A made-up "0.8g CO₂ per page view" is worse than nothing, because people will repeat it.
3. **Willing to say no.** Sometimes the lowest-impact version of a feature is not building it, or building something much smaller. Ephemeralization applies to scope, too. Say so plainly when it's warranted, and offer the smaller alternative.
4. **No greenwashing boilerplate.** Generic advice ("optimize images", "use green hosting") that ignores the specific design is noise. Every finding should point at something in *this* design. If a common mitigation genuinely applies, tie it to the specific asset, flow, or component.
5. **Name trade-offs.** Sustainability often competes with accessibility, inclusion, safety, or business goals. Accessibility is not negotiable — never recommend a change that breaks contrast, legibility, reduced-motion support, or older-device access in the name of efficiency. Surface the other tensions; let the humans decide.

## Workflow

### 1. Understand the design (brief intake)

Get enough to reason concretely. Pull what you can from the conversation, files, Figma links, or the repo first; ask only for gaps that would change the verdict. Usually you need:

- **What** is being designed and the **job** it does for people. What problem does it solve — and is that the root problem?
- **Type:** digital-only, or phygital (has hardware, print, packaging, installations, or physical logistics)?
- **Scale and lifespan:** rough audience size, frequency of use, how long it is expected to live, how often content/hardware will be refreshed.
- **Context:** who's affected beyond the direct user (staff, communities, suppliers, people near a physical installation, people on older devices or slow networks).
- **Constraints:** what's already decided vs. still open.

If the user wants a fast pass, make sensible assumptions, list them in the plan, and proceed — don't block on a questionnaire.

### 2. Map the system and the critical path

Sketch the whole system the design touches (Fuller's comprehensive view): the people, devices, networks, servers/services, physical materials, and the before/after of its life. Then identify the **critical path** — the few decisions that gate everything downstream and are hardest to reverse (e.g., "requires an always-on cloud connection", "ships a dedicated device", "autoplay video as the hero", "new app instead of web"). These go first in the plan.

### 3. Run the lenses

Work through each lens, but only report findings that are actually relevant to this design — skip empty sections rather than padding them.

- **Lifecycle** — creation → delivery → use → longevity → end of life. For digital work read `references/digital.md`; for anything with a physical component also read `references/phygital.md`.
- **Behavior** — what the design encourages people to do. Does it drive overconsumption (infinite scroll, autoplay, streaks, notifications, frequent upgrades, disposable add-ons)? Is the lower-impact choice the default and the easy path? Norman's signifiers and defaults matter here: what the design *suggests* is what people will do at scale. Look at it as Meadows would: which reinforcing loops amplify use or cost, which balancing loops (budgets, limits, stops) hold them in check, and how long the delay is before anyone sees the consequence.
- **System & community** — who bears costs that don't show up on the project's books (externalities)? Does it lock people in, make things obsolete, shift labor or waste elsewhere? Could the community it affects help shape it?
- **Measurement** — what would tell you, after launch, whether the design is doing better or worse than expected? Prefer a few honest metrics the team can actually collect over an impressive dashboard nobody maintains.

### 4. Find the trimtabs

From everything above, choose the **top 1–3 leverage points**: changes that are small relative to their effect, ideally ones that make good behavior the default. Rank by (impact reduced) × (still changeable now) ÷ (effort). This is the heart of the plan; be specific.

Label each trimtab with its place on Meadows' ladder (see `references/frameworks.md`), e.g. "rules / defaults (5)" or "parameter (12)". If every trimtab is a parameter tweak, look again for a stronger lever: a default or rule, an information flow that makes the cost visible, a limit on a runaway loop, or the goal itself. Name it even if it's harder, and let the team choose. Check that each lever is pulled in the right direction.

### 5. Translate to design tokens where it fits

Many digital mitigations are best encoded once in the design system rather than re-decided screen by screen. When a finding maps to tokens, recommend the concrete token change. Read `references/tokens.md` for the patterns (motion, color/dark themes, typography, effects, sizes/breakpoints, a low-impact mode). If you're working in a token repository, look at the actual token files and refer to real token names.

### 6. Write the plan

**Default to the one-page brief** in `references/plan-template.md`: 650–700 words (300–450 for a Build verdict), leading with the verdict and the trimtabs. A plan only changes decisions if people read it, and long plans don't get read: earlier versions of this skill produced 2,000+ word plans that buried their best ideas. Do the full analysis anyway — every lens, every stage — then keep only what changes a decision. Write the **full plan** (same file, second template) only when the user asks for it or the plan is headed for a formal review; otherwise end by offering it in one line.

**Verdict** — pick one and justify it in a sentence or two:
- **Build** — impact is proportionate to the value; note the minor improvements.
- **Build differently** — worth doing, but one or more critical-path decisions should change.
- **Reconsider** — the value is unclear relative to the cost, or a much smaller version would do most of the job. Propose that version.
- **Don't build** — the root problem is better solved another way, or the harm clearly outweighs the benefit. Propose what to do instead.

**Figures:** when saving the plan as a file, also render its figures: the **leverage ladder** (trimtabs on Meadows' rungs), the **lifecycle strip** (impact tier and confidence per stage) and, when the behavior lens found real feedback loops, the **loop map** (reinforcing loops and the balancing loops that check them). Write a small JSON summary from the finished plan and run `scripts/render_visuals.py`; `references/visuals.md` has the format and where to embed them. The script draws them the same way every time, so don't hand-draw SVG.

**Where to put it:** If the user is working in a repository or folder, save the plan as a markdown file (default `impact-plans/<short-slug>.md`, or wherever they prefer) so it can be versioned and shared, and give a short summary in chat. Otherwise present it in the conversation. If they plan to share it with collaborators, offer to publish it as a page or document.

## Revisiting a plan

Plans should travel with the design. If an existing plan is provided and the design has changed, update it rather than starting over: note what changed, re-check the critical path, and keep a short dated changelog at the bottom.
