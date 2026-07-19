#!/usr/bin/env python3
"""Build the deterministic Trump Groove README promo banner."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
WIDTH, HEIGHT = 1600, 900
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def cover(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    scale = max(size[0] / image.width, size[1] / image.height)
    resized = image.resize(
        (round(image.width * scale), round(image.height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - size[0]) // 2
    top = (resized.height - size[1]) // 2
    return resized.crop((left, top, left + size[0], top + size[1]))


def fit_subject(path: Path, height: int) -> Image.Image:
    image = Image.open(path).convert("RGBA")
    bbox = image.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError(f"Empty subject: {path}")
    subject = image.crop(bbox)
    scale = height / subject.height
    return subject.resize(
        (round(subject.width * scale), height), Image.Resampling.LANCZOS
    )


def center_text(
    draw: ImageDraw.ImageDraw,
    y: int,
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
    *,
    stroke_width: int = 0,
    stroke_fill: tuple[int, int, int, int] | None = None,
) -> None:
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    x = (WIDTH - (box[2] - box[0])) // 2
    draw.text(
        (x, y),
        text,
        font=font,
        fill=fill,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )


def main() -> None:
    background = cover(
        Image.open(ASSETS / "source" / "promo-background.png").convert("RGBA"),
        (WIDTH, HEIGHT),
    )
    canvas = background.copy()

    # Deterministic contrast overlays keep exact title and footer copy readable.
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    overlay_px = overlay.load()
    for y in range(250):
        alpha = round(185 * (1 - y / 250) ** 1.6)
        for x in range(WIDTH):
            overlay_px[x, y] = (2, 10, 35, alpha)
    ImageDraw.Draw(overlay).rectangle((0, 842, WIDTH, HEIGHT), fill=(2, 10, 35, 220))
    canvas = Image.alpha_composite(canvas, overlay)

    title_font = ImageFont.truetype(FONT_BOLD, 102)
    subtitle_font = ImageFont.truetype(FONT_BOLD, 30)
    label_font = ImageFont.truetype(FONT_BOLD, 22)
    footer_font = ImageFont.truetype(FONT_REGULAR, 24)
    draw = ImageDraw.Draw(canvas)
    center_text(
        draw,
        34,
        "TRUMP GROOVE",
        title_font,
        (255, 248, 226, 255),
        stroke_width=3,
        stroke_fill=(5, 22, 67, 255),
    )
    center_text(
        draw,
        145,
        "THE CODEX PET WITH MEME ENERGY",
        subtitle_font,
        (255, 195, 65, 255),
        stroke_width=1,
        stroke_fill=(5, 22, 67, 255),
    )

    cards = [
        ("SMIRK", ASSETS / "emotes" / "smirk.png", 365, 236),
        ("THUMBS UP", ASSETS / "emotes" / "thumbs-up.png", 365, 608),
        ("SHRUG", ASSETS / "emotes" / "shrug.png", 335, 990),
        ("TRUMP DANCE", ASSETS / "emotes" / "trump-dance-pose.png", 405, 1360),
    ]
    baseline = 790

    for label, path, subject_height, center_x in cards:
        subject = fit_subject(path, subject_height)
        x = round(center_x - subject.width / 2)
        y = baseline - subject.height

        shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        mask = subject.getchannel("A").filter(ImageFilter.GaussianBlur(14))
        shadow_color = Image.new("RGBA", subject.size, (0, 10, 40, 180))
        shadow_color.putalpha(mask.point(lambda value: round(value * 0.58)))
        shadow.alpha_composite(shadow_color, (x + 8, y + 12))
        canvas = Image.alpha_composite(canvas, shadow)
        canvas.alpha_composite(subject, (x, y))

        label_w = max(170, round(label_font.getlength(label)) + 42)
        label_x = round(center_x - label_w / 2)
        label_y = 794
        label_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        label_draw = ImageDraw.Draw(label_layer)
        label_draw.rounded_rectangle(
            (label_x, label_y, label_x + label_w, label_y + 40),
            radius=20,
            fill=(3, 17, 58, 225),
            outline=(255, 192, 55, 255),
            width=2,
        )
        text_box = label_draw.textbbox((0, 0), label, font=label_font)
        label_draw.text(
            (
                round(center_x - (text_box[2] - text_box[0]) / 2),
                label_y + 7,
            ),
            label,
            font=label_font,
            fill=(255, 250, 236, 255),
        )
        canvas = Image.alpha_composite(canvas, label_layer)

    draw = ImageDraw.Draw(canvas)
    center_text(
        draw,
        858,
        "codex-pets.net/#/pets/trump-groove",
        footer_font,
        (221, 233, 255, 255),
    )

    output = ASSETS / "trump-groove-promo.png"
    canvas.convert("RGB").save(output, optimize=True)
    manifest = {
        "output": str(output.relative_to(ROOT)),
        "size": [WIDTH, HEIGHT],
        "exact_text": [
            "TRUMP GROOVE",
            "THE CODEX PET WITH MEME ENERGY",
            "SMIRK",
            "THUMBS UP",
            "SHRUG",
            "TRUMP DANCE",
            "codex-pets.net/#/pets/trump-groove",
        ],
        "subject_sources": [str(path.relative_to(ROOT)) for _, path, _, _ in cards],
        "background_source": "assets/source/promo-background.png",
        "composition": "deterministic Pillow overlay; character pixels are not regenerated",
    }
    (ASSETS / "promo-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
