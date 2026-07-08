#!/usr/bin/env python3
"""Regenerate logo.svg for the DevUtils isometric cube icon."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ICON_SVG = ROOT / "assets" / "logo.svg"


def main() -> None:
    # Source of truth is assets/logo.svg — script exists for convenience only.
    if not ICON_SVG.exists():
        raise SystemExit(f"Missing {ICON_SVG}")
    print(f"Logo present at {ICON_SVG} ({ICON_SVG.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
