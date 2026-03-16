#!/usr/bin/env python3
"""
get_city_tokens.py — Extract color tokens (and optionally texture CSS) for a city.

Usage:
  python3 get_city_tokens.py "京都"           # color tokens (shell eval-friendly)
  python3 get_city_tokens.py "Kyoto"          # case-insensitive, Chinese or English
  python3 get_city_tokens.py "京都" --texture  # print only the CSS texture block

Color output (one token per line, for shell eval):
  CITY_BG=#f7f0e6
  CITY_SURFACE=#ede4d6
  CITY_INK=#2a1f14
  CITY_MUTED=#7a6655
  CITY_ACCENT=#8b4513

Exit 0 on success, 1 if city not found.
"""

import sys
import re
from pathlib import Path

CITY_STYLES = Path(__file__).parent.parent.parent / "references" / "city-styles.md"

# Map CSS variable names → output key names
VAR_MAP = {
    "--bg":         "CITY_BG",
    "--bg-surface": "CITY_SURFACE",
    "--ink":        "CITY_INK",
    "--ink-muted":  "CITY_MUTED",
    "--accent":     "CITY_ACCENT",
}


def find_city_section(text: str, query: str) -> str | None:
    """Return the markdown text of the matching city section, or None."""
    query_lower = query.lower().strip()
    # Split on ## headings (city sections)
    sections = re.split(r"\n(?=## \d+\.)", text)
    for section in sections:
        first_line = section.split("\n")[0]
        if query_lower in first_line.lower():
            return section
    return None


def extract_colors(section: str) -> dict:
    """Parse the ### Colors block and return {VAR_MAP key: value}."""
    result = {}
    in_colors = False
    for line in section.splitlines():
        if re.match(r"^### Colors", line):
            in_colors = True
            continue
        if in_colors and re.match(r"^### ", line):
            break  # next subsection
        if in_colors:
            for css_var, out_key in VAR_MAP.items():
                # Match: --bg:    #xxx  or  --bg:  rgba(...)
                pattern = rf"^\s*{re.escape(css_var)}\s*:\s*([#\w(),.\s%]+)"
                m = re.match(pattern, line)
                if m:
                    value = m.group(1).split("/*")[0].strip().rstrip(",")
                    result[out_key] = value
    return result


def extract_texture(section: str) -> str:
    """Return the CSS inside the ### Texture code block, or empty string."""
    m = re.search(r"### Texture.*?```css\s*(.*?)```", section, re.S)
    return m.group(1).strip() if m else ""


def main():
    if len(sys.argv) < 2:
        print("Usage: get_city_tokens.py <city-name> [--texture]", file=sys.stderr)
        sys.exit(1)

    query = sys.argv[1]
    want_texture = "--texture" in sys.argv

    text = CITY_STYLES.read_text(encoding="utf-8")
    section = find_city_section(text, query)

    if not section:
        print(f"City not found: {query}", file=sys.stderr)
        sys.exit(1)

    if want_texture:
        css = extract_texture(section)
        if css:
            print(css)
        else:
            print(f"No texture block found for '{query}'", file=sys.stderr)
            sys.exit(1)
        return

    colors = extract_colors(section)

    missing = [k for k in VAR_MAP.values() if k not in colors]
    if missing:
        print(f"Warning: could not parse {missing} for '{query}'", file=sys.stderr)

    for key in VAR_MAP.values():
        if key in colors:
            print(f"{key}={colors[key]}")


if __name__ == "__main__":
    main()
