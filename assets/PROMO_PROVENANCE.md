# Promotional image provenance

The README hero is a deterministic composite designed to preserve the supplied Trump Groove character art exactly.

## Generated layer

- Mode: built-in Codex ImageGen
- Use case: `ads-marketing`
- Scope: abstract background only
- Prompt summary: energetic navy, electric-blue, red, and gold dance-stage background with four placement zones; no characters, text, logos, icons, or political campaign branding.

## Deterministic layers

- Exact title, subtitle, pose labels, and URL are rendered by `scripts/build_promo.py`.
- Smirk, thumbs-up, shrug, and Trump Dance subjects are composited from the transparent PNGs under `assets/emotes/`.
- All four subjects are normalized to the same 365 px visible height and aligned to the same shoe baseline.
- Character identity, expressions, poses, clothing, proportions, and source pixels are not regenerated.
- Final export: `assets/trump-groove-promo.png`, 1600 × 900 RGB PNG.

The exact source list, copy, and export dimensions are recorded in `assets/promo-manifest.json`.
