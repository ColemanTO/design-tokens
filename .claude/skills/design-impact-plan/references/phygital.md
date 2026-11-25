# Phygital lifecycle checklist

For designs that combine digital and physical: connected/IoT products, kiosks and screens, retail and event installations, smart or QR/AR packaging, wearables, printed material that links to digital experiences. Read `digital.md` too — the digital half still applies.

## Contents
- Why phygital is different
- Materials and manufacturing
- Energy in use
- Connectivity and the cloud dependency trap
- Repair, upgrade, and support
- Packaging and print
- Installations, events, and retail
- End of life
- Regulations to check

## Why phygital is different

Physical things carry **embodied impact** that's paid up front and can't be optimized away later; a lot of their lifetime cost is decided at design time. And when physical things depend on digital services, the **weakest-lived component sets the lifespan of the whole**: a sturdy device becomes e-waste when its app or cloud is shut down. Fuller's "no away" is literal here.

Questions to start with:
- Does this need to be a physical thing at all? Could an existing device (the user's phone, an existing screen) do the job? (ephemeralization)
- If it must be physical, could it be shared, rented, reused, or designed for a second life?

## Materials and manufacturing
- Dedicated electronics vs. reusing commodity hardware.
- Batteries: replaceable or glued in? Rechargeable vs. disposable? Could it run without one (mains, energy harvesting, passive NFC)?
- Material choices: recycled content, mono-materials that can actually be recycled, avoiding mixed laminates and hard-to-separate composites.
- Overspecification: more sensors, screen, or compute than the job needs.

## Energy in use
- Always-on screens and kiosks: brightness, sleep/wake on presence, scheduled off-hours, e-ink or reflective displays for mostly static content.
- Standby/idle power across the fleet (small per unit × many units × years).
- Lighting, heating, cooling for installations.

## Connectivity and the cloud dependency trap
- Does core function require the cloud, or does it work locally with cloud as an enhancement? Local-first protects longevity.
- What happens if the vendor's service shuts down? Is there an open protocol, local API, or published end-of-life plan so devices keep working?
- Network chattiness: telemetry frequency, firmware download size and cadence.

## Repair, upgrade, and support
- Can users or local repairers open it, get parts, and find documentation?
- How many years of security and firmware updates are committed? Is that stated to buyers?
- Modularity: can the part that ages fastest (battery, screen, radio) be swapped without replacing the whole?

## Packaging and print
- Right-sized, minimal, recyclable packaging; avoid plastic windows, foils, and mixed materials.
- **QR codes replacing printed manuals** reduce paper but move cost to a service that must stay online and readable for the product's whole life, and exclude people without smartphones or connectivity. Keep essential safety and setup info physical; host digital content on durable URLs.
- AR packaging experiences: is the experience worth the asset weight and the device energy, and will anyone use it twice?
- Print runs: on-demand vs. bulk; what happens to leftovers?

## Installations, events, and retail
- Build for reuse: modular structures, rented AV, standard screen sizes, content that can be updated without new hardware.
- Transport and logistics of materials and people.
- Plan the strike: what happens to everything the day after? Who takes it, and where does it go?
- Single-use giveaways, wristbands, badges with chips.

## End of life
- Take-back or trade-in program? Refurbishment path?
- Data wiping for devices that collect personal data.
- Battery and e-waste handling instructions on the product, not just online.

## Regulations to check
Mention these as things to verify, not as legal advice; requirements and dates change:
- EU **Ecodesign for Sustainable Products Regulation (ESPR)** and **Digital Product Passports**.
- EU **right-to-repair** rules and ecodesign requirements for phones/tablets (spare parts, update support periods).
- EU **battery regulation** (replaceability, labeling).
- **WEEE** and national/state e-waste and extended producer responsibility laws.
- Packaging regulations (e.g., the EU Packaging and Packaging Waste Regulation, state EPR laws in the US).
