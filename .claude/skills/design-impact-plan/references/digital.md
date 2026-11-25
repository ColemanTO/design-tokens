# Digital lifecycle checklist

A prompt list, not a form. Use what is relevant to the design in front of you, and tie every finding to a specific screen, asset, flow, or component.

## Contents
- How digital impact actually adds up
- Creation
- Delivery (network and server)
- Use (device energy)
- Longevity (devices and support)
- End of life (data and deprecation)
- Behavior patterns to watch
- Methodologies you can cite

## How digital impact actually adds up

Keep the big picture in mind so effort goes where it matters:

- **Devices dominate.** For most consumer electronics, the majority of lifetime emissions come from *manufacturing* the device, not from using it. So a design that pushes people to upgrade (by requiring new OS versions, more memory, faster chips) can outweigh every byte you save. **Supporting older devices and slow networks is often the biggest lever**, and it is also an inclusion win.
- **Data transfer and server work scale with use.** A small saving on a page loaded millions of times adds up; a big saving on a rarely used admin screen doesn't.
- **Video, autoplay, and always-on background activity** (polling, tracking, sync) are usually the heaviest everyday costs.
- **Third-party scripts** (ads, analytics, chat widgets, A/B tools) are often heavier than the product itself, and they're invisible in design files.

## Creation
- Is this a new thing, or can an existing pattern, component, or page do the job? Reuse is ephemeralization.
- Heavy production assets (3D, video shoots, generative-AI imagery at volume) — are they essential to the job?
- Will AI features run large models on every interaction when a lighter approach would do? Can inference be cached, batched, made opt-in, or done on-device?

## Delivery (network and server)
- **Page/screen weight:** images (format, sizing, lazy-loading), video, fonts (number of families and weights, subsetting, system font option), icon sets, JS bundles.
- **Autoplay media**, carousels with heavy slides, background video heroes.
- **Third parties:** what's added beyond the design itself?
- **Caching and offline:** can repeat visits avoid re-downloading? Does an offline-first approach fit?
- **Real-time features:** websockets/polling where periodic or on-demand updates would do.
- **Hosting:** location, renewable energy commitments (check the Green Web Foundation directory), right-sized infrastructure. Mention only if the team controls it.
- **Data retention and storage:** storing everything forever (logs, uploads, analytics) has ongoing cost.

## Use (device energy)
- **Dark themes** save meaningful energy only on OLED/AMOLED screens, and mostly at higher brightness. Offer it, respect the system setting, but don't overclaim. Keep it accessible: near-black backgrounds with sufficient contrast, not pure-black-with-pure-white glare.
- **Animation and effects:** continuous animations, parallax, large blurs (`backdrop-filter`), heavy shadows, and video backgrounds keep the GPU busy. Respect `prefers-reduced-motion`; avoid infinite loops for decoration.
- **Background work:** location tracking, sync frequency, push notifications, wake locks.
- **Session length by design:** is the product designed to maximize time-on-app? That is an energy and attention cost.

## Longevity (devices and support)
- Which devices, OS versions, and browsers are supported? Does the design require recent hardware (heavy WebGL, large memory, new APIs) without a graceful fallback?
- Does it work on slow or metered connections? Progressive enhancement?
- Will design or app updates push users toward upgrades?
- Is it built from durable, maintainable parts (the design system) or one-off code that will be rewritten soon?

## End of life (data and deprecation)
- What happens when the feature or product is retired? Is user data exportable and deleted on schedule?
- Do connected devices or integrations depend on this service? (If so, see phygital.md: retiring a service can turn hardware into waste.)
- Is there a sunset plan for campaign sites, microsites, and experiments that otherwise live forever?

## Behavior patterns to watch
- Infinite scroll, autoplay-next, streaks, variable rewards, notification pressure.
- "Upgrade" nudges, accessory/consumable upsells, disposable defaults (e.g., new account per event).
- Defaults that matter at scale: video quality, auto-download, sync frequency, delivery speed in e-commerce (express shipping as default), printing receipts.
- Opportunities: make the low-impact choice the default and visible (e.g., standard shipping preselected with an honest explanation, "download on Wi-Fi only" on by default).

## Methodologies you can cite
Only give numbers you can trace to one of these (or to user-supplied data), and show the inputs:
- **Sustainable Web Design model** (sustainablewebdesign.org) — estimates emissions from data transfer; implemented in **CO2.js** by the Green Web Foundation.
- **W3C Web Sustainability Guidelines (WSG)** — a broad, evidence-linked guideline set useful for checklists and citations.
- Lighthouse / WebPageTest for real page weight and request counts on an existing build.
- Device manufacturers' product environmental reports for embodied emissions of specific hardware.

Models like these are estimates with wide uncertainty; say so. Relative comparisons ("this hero video roughly triples the page weight") are usually more honest and more useful than absolute grams.
