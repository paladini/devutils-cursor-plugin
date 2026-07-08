#!/usr/bin/env python3
"""Generate a terminal-style demo GIF for the DevUtils MCP Server README."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "devutils-mcp-server" / "assets" / "demo.gif"

W, H = 920, 520
BG = (15, 23, 42)
PANEL = (30, 41, 59)
GREEN = (52, 211, 153)
CYAN = (34, 211, 238)
BLUE = (96, 165, 250)
YELLOW = (250, 204, 21)
GRAY = (148, 163, 184)
WHITE = (226, 232, 240)
RED = (248, 113, 113)

SCENES = [
    [
        ("$ npx -y devutils-mcp-server", CYAN),
        ("DevUtils MCP Server running on stdio", GREEN),
        ("36 tools ready · hash · encode · uuid · jwt · json · network · text", GRAY),
    ],
    [
        ('> "Generate 3 UUID v4 values"', BLUE),
        ("→ generate_uuid(count=3)", YELLOW),
        ("  7c9e6679-7425-40de-944b-e07fc1f90ae7", WHITE),
        ("  550e8400-e29b-41d4-a716-446655440000", WHITE),
        ("  f47ac10b-58cc-4372-a567-0e02b2c3d479", WHITE),
    ],
    [
        ('> "Decode this JWT and check expiration"', BLUE),
        ("→ jwt_decode(...)", YELLOW),
        ('  header: {"alg":"HS256","typ":"JWT"}', WHITE),
        ('  payload: {"sub":"user_42","exp":"2026-12-31T23:59:59Z"}', WHITE),
        ("  status: valid · not expired", GREEN),
    ],
    [
        ('> "Pretty-print and validate this JSON"', BLUE),
        ("→ json_validate · json_format", YELLOW),
        ('  { "name": "devutils", "tools": 36, "local": true }', WHITE),
        ("  valid JSON · 3 keys", GREEN),
    ],
]


def load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for name in ("Consolas", "Cascadia Mono", "Courier New", "DejaVuSansMono.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_frame(scene_idx: int, progress: float) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle((24, 24, W - 24, H - 24), radius=18, fill=PANEL, outline=(51, 65, 85))

    title_font = load_font(22)
    body_font = load_font(18)
    small_font = load_font(15)

    draw.text((48, 42), "DevUtils MCP Server", font=title_font, fill=WHITE)
    draw.text((48, 72), "Local developer utilities for AI agents", font=small_font, fill=GRAY)

    y = 118
    visible_lines = max(1, int(len(SCENES[scene_idx]) * progress))
    for i, (line, color) in enumerate(SCENES[scene_idx][:visible_lines]):
        prefix = "  "
        if i == visible_lines - 1 and progress < 1:
            dots = "." * (1 + int((progress * 3) % 3))
            line = line + dots
        draw.text((48, y), prefix + line, font=body_font, fill=color)
        y += 34

    draw.text((48, H - 58), "npx -y devutils-mcp-server  ·  zero API keys  ·  runs locally", font=small_font, fill=GRAY)

    pulse = 0.5 + 0.5 * math.sin(progress * math.pi * 2)
    dot = int(180 + 60 * pulse)
    draw.ellipse((W - 72, 42, W - 48, 66), fill=(dot, 211, 153))

    return img


def main() -> None:
    frames: list[Image.Image] = []
    for scene_idx in range(len(SCENES)):
        for step in range(12):
            frames.append(draw_frame(scene_idx, min(1.0, (step + 1) / 10)))
        for _ in range(8):
            frames.append(draw_frame(scene_idx, 1.0))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        OUT,
        save_all=True,
        append_images=frames[1:],
        duration=180,
        loop=0,
        optimize=True,
    )
    print(f"Wrote {OUT} ({len(frames)} frames)")


if __name__ == "__main__":
    main()
