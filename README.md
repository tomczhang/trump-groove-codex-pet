<p align="center">
  <img src="assets/trump-groove-promo.png" alt="Trump Groove — Smirk, Thumbs Up, Shrug, and Trump Dance" width="100%" />
</p>

<h1 align="center">Trump Groove</h1>

<p align="center">
  A high-energy Codex Pet with expressive reactions, meme energy, and a hypnotic six-beat Trump Dance.
</p>

<p align="center">
  <a href="https://codex-pets.net/#/pets/trump-groove"><strong>View Trump Groove on Codex Pets →</strong></a>
</p>

## Preview

<p align="center">
  <img src="assets/trump-dance.gif" alt="Trump Groove dance animation" width="360" />
</p>

The `running` state uses a deliberately tuned six-beat loop:

```text
pose 1 → pose 2 → pose 2 → pose 1 → pose 3 → pose 3
```

This gives the arm-folding dance a catchy hold-and-release rhythm instead of a mechanically even frame cadence.

## Highlights

- **Signature Trump Dance** — a hand-tuned arm-folding groove used as the active `running` animation.
- **Expressive personality** — smirk, thumbs-up, shrug, review, waiting, success/failure, and directional movement states.
- **Codex Pet V2 ready** — `spriteVersionNumber: 2` with a `1536 × 2288` RGBA WebP atlas.
- **Complete animation set** — nine standard Codex states plus sixteen clockwise look directions.
- **Pet-size readability** — smooth transparent edges, compact silhouette, and bold colors designed to remain legible at small sizes.

## Install

### 1. Clone the repository

```bash
git clone https://github.com/tomczhang/trump-groove-codex-pet.git
cd trump-groove-codex-pet
```

SSH users can instead clone with `git@github.com:tomczhang/trump-groove-codex-pet.git`.

### 2. Copy the Pet resources

```bash
mkdir -p ~/.codex/pets/trump-groove
cp pet.json spritesheet.webp ~/.codex/pets/trump-groove/
```

### 3. Activate Trump Groove

Open the Pet picker in Codex and select **Trump Groove**. If the new Pet does not appear immediately, switch to another Pet and back again, or restart Codex once to refresh the local Pet registry.

## Repository layout

```text
.
├── pet.json                    # Pet identity and V2 metadata
├── spritesheet.webp            # 8 × 11 Codex Pet V2 animation atlas
├── assets/
│   ├── trump-groove-promo.png  # README promotional artwork
│   ├── trump-dance.gif         # Running-state dance preview
│   └── emotes/                 # Source poses used in the promo artwork
└── scripts/
    └── build_promo.py          # Deterministic promo compositor
```

## 中文说明

**Trump Groove** 是一个带有“魔性律动”的 Codex Pet。它最突出的特点是 `running` 状态下的六拍 Trump Dance，通过重复关键动作形成更有节奏感的停顿与摆动。

使用方法：把根目录中的 `pet.json` 和 `spritesheet.webp` 复制到 `~/.codex/pets/trump-groove/`，然后在 Codex 的 Pet 选择器中选择 **Trump Groove**。

在线查看：[codex-pets.net/#/pets/trump-groove](https://codex-pets.net/#/pets/trump-groove)

## Disclaimer

This is an unofficial, fan-made caricature Pet created for playful and parody use. It is not affiliated with or endorsed by Donald Trump, OpenAI, or the Codex Pets website.
