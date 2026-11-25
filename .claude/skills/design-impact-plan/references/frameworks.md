# The lenses behind the skill

Use this to explain *why* a recommendation matters, or to give collaborators a shared vocabulary. Paraphrase in plain language; don't attribute exact quotes unless you are certain of the wording.

## Don Norman — *Design for a Better World* (2023)

Norman argues that much of today's harm comes from designing for the wrong measures (short-term profit, engagement, GDP) and for the individual "user" while ignoring everyone and everything else. His alternative is **humanity-centered design**. Its working principles, paraphrased:

1. **Solve the core (root) problem**, not the symptom. Ask "why?" until you reach the real need. Many products exist to treat problems that a different design upstream would have prevented.
2. **Focus on the entire ecosystem.** Every design sits inside larger systems — social, economic, ecological. Consider the people who make, maintain, live near, and dispose of it, not just the people who use it.
3. **Think long term.** Who will be living with this in ten years? What does it do when it breaks, is no longer supported, or is thrown away?
4. **Test and refine continually; work in small, modular steps.** Big-bang solutions to complex problems usually fail. Prefer incremental, reversible changes that can be learned from.
5. **Design with the community.** The people affected often understand the problem best. Facilitate their participation; don't impose expert solutions.

Related themes worth drawing on:
- **Measure what matters.** Choose metrics that reflect human and planetary well-being, not just growth.
- **Circularity and repair.** Design for reuse, repair, refurbishment and recovery rather than a take–make–waste line. Resist planned obsolescence, including the software kind (dropping support, forced upgrades).
- **Meaning over consumption.** Designs that encourage endless consumption trade long-term well-being for short-term metrics.

How it shows up in a plan: root-problem check in the intake, the system & community lens, longevity and end-of-life findings, the behavior lens, honest metrics, small reversible steps in the recommendations.

## Buckminster Fuller — *Critical Path* (1981)

Fuller saw design as a way to make the world work for everyone with the resources we have, and called this **comprehensive anticipatory design science**.

- **Comprehensive:** think about the whole system first. Specialization makes people blind to the effects of their part on the whole.
- **Anticipatory:** solve problems before they arrive, through design, rather than react to them afterward.
- **Spaceship Earth:** a closed system with finite resources and no "away" to throw things. Every byproduct lands somewhere.
- **Ephemeralization:** technology tends to do more and more with less and less (material, energy, time). Good design rides this curve — less mass, fewer resources, more performance. Applied to scope: the best feature may be a smaller one, or none.
- **Trimtab:** the small tab on a ship's rudder that turns the rudder that turns the ship. Look for the small, well-placed intervention with outsized effect — often a default, a constraint, or a shared system component (like a design token).
- **Critical path:** in any large undertaking, some tasks must come before others and gate everything downstream. Identify and sequence those first.
- **Synergy:** whole-system behavior can't be predicted from the parts alone. Check how components interact, not just each one in isolation.

How it shows up in a plan: the system map, the critical-path section, the trimtabs, the "less is more" bias in recommendations, the willingness to say "don't build", and the use of design tokens as leverage points.

## Donella Meadows — *Thinking in Systems* (2008) and "Leverage Points: Places to Intervene in a System" (1999)

Meadows was a systems scientist and lead author of *The Limits to Growth*. Her leverage-points essay ranks the places to intervene in a system from least to most effective. It turns Fuller's trimtab from a metaphor into a ladder you can climb. Her ordering, from weakest (12) to strongest (1), with what each means in design:

| # | Leverage point | In a design |
|---|----------------|-------------|
| 12 | Constants, parameters, numbers | Page weight, bitrate, screen brightness, a token's value. Easy to change and usually the weakest. |
| 11 | Sizes of buffers relative to flows | Caches, offline storage, spare-parts stock, battery capacity. |
| 10 | Structure of material stocks and flows | Architecture and physical infrastructure: device fleets, a chip in every unit, where data lives. Very hard to change once built, so it belongs on the critical path. |
| 9 | Lengths of delays | How long before anyone sees the consequence: e-waste years later, a cloud bill next quarter, a metric nobody checks. |
| 8 | Strength of balancing feedback loops | Limits that correct drift: performance budgets enforced in CI, autoplay that stops, rate limits, update-support commitments. |
| 7 | Gain of reinforcing feedback loops | Loops that amplify: engagement mechanics, costs that grow with every visit, upgrade cycles. Slowing a runaway loop beats tuning its parameters. |
| 6 | Structure of information flows | Who can see the cost: showing users their data use, putting page weight on the team dashboard, disclosing AI imagery, labeling repairability. |
| 5 | Rules of the system | Defaults, design-system rules, token *modes*, policies ("no autoplay"), procurement criteria. |
| 4 | Power to add, change or self-organize structure | Letting users, repairers and communities adapt the system: open protocols, local-first, repair docs, design-system governance. |
| 3 | Goals of the system | What the product optimizes: engagement or outcome? Growth or sufficiency? (Norman's "measure what matters".) |
| 2 | The mindset or paradigm the system comes from | "New is better", "more features is better", disposability as normal. |
| 1 | The power to transcend paradigms | Holding any model loosely; staying open to "we don't need this at all". |

Two of her observations matter in practice:
- **People push leverage points in the wrong direction.** Teams often find the right lever and pull it the wrong way: more engagement to fund sustainability work, bigger caches that keep stale heavy assets around. Check the direction, not just the point.
- **Lower numbers are stronger but harder.** Most recommendations land at 12–8, and that's fine. The point is to notice when a 5, 3 or 2 is available, and to say so, even if the team chooses the easier lever.

How it shows up in a plan: each trimtab is labeled with its leverage level; the behavior lens looks for reinforcing and balancing loops and for delays; information-flow fixes (making cost visible) are treated as real interventions, not afterthoughts.

## Where they agree

All three reject the idea that the designer's responsibility ends at the user's screen or the product's box. All favor anticipation over cleanup, whole systems over parts, and doing more good with less stuff. Norman adds the human and community side — participation, meaning, behavior; Fuller adds the resource accounting and the engineering instinct for leverage and sequence; Meadows adds the systems vocabulary — stocks, flows, loops, delays — and a ranking of where change actually takes hold.
