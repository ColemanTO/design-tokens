# Design tokens as trimtabs

A design token decides something once for every screen that uses it. That makes tokens one of the best leverage points in digital design: change a default in the system, and every product built on it inherits the improvement. Recommend token changes when a finding is systemic (appears across screens or products), not for one-off issues.

When working in a token repository, read the actual token files and use real token names and structure. This repository's Figma plugin exports tokens in categories like color, typography (fonts), effects, motion, grids, sizes, spacing, breakpoints, borders, radii, and opacity, and it supports **Figma variable modes**, which makes a mode-based approach natural.

## Patterns

### Motion
- Shorter default durations; avoid decorative infinite loops.
- A reduced-motion set (duration ≈ 0 or crossfade only) that code maps to `prefers-reduced-motion`. This is an accessibility requirement as well as an energy saving.
- Name tokens by intent (`motion.feedback`, `motion.transition.page`) so heavy motion can't sneak in as an ad-hoc value.

### Color and themes
- A dark theme tuned for OLED: near-black surfaces (not pure #000 against pure white text, which causes halation for some readers) with contrast that still meets WCAG.
- Wire themes to the system preference by default.
- Be honest about the size of the saving: meaningful on OLED at higher brightness, negligible on LCD.

### Typography
- A system font stack token as an option or default for body text; it removes font downloads entirely.
- If brand fonts are required, limit families and weights in the token set (each weight is a file), prefer variable fonts, and note subsetting.

### Effects
- Prefer light shadows over large blurs; limit `backdrop-filter` blur tokens, which keep the GPU busy, especially on scroll.
- A small, fixed set of elevation tokens rather than many bespoke effects.

### Sizes and breakpoints
- Breakpoint and size tokens can drive responsive image sizes (`srcset`/`sizes`) so smaller screens download smaller images.
- Media aspect-ratio tokens help avoid layout shift and oversize assets.

### Opacity and imagery
- Avoid patterns that layer full-bleed images under heavy overlays when a solid or gradient token would do.

### A low-impact mode
Using variable modes (e.g., a `low-impact` or `lite` mode alongside `light`/`dark`), define one coherent set: system fonts, reduced motion, no blur effects, a dark OLED-friendly palette, and smaller media sizes. Products can switch it on automatically (on `prefers-reduced-data`, Save-Data, or low battery where available) or let users choose it. Treat it as a progressive enhancement and test it for accessibility like any other mode.

## How to write the recommendation
Be concrete: which token or group, what value or new mode, which findings it addresses, and the trade-off. For example:

> **motion.duration.*:** add a `reduced` mode with 0ms durations except `motion.feedback` (100ms crossfade). Addresses the always-animating hero and the scroll parallax; also delivers `prefers-reduced-motion` support. Trade-off: the brand team will want a review of the hero entrance.
