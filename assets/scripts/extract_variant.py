#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

START_RE = re.compile(r"^\s*<!--\s*@@VARIANT:([A-Za-z0-9_]+)\s*-->\s*$")
END_RE = re.compile(r"^\s*<!--\s*@@/VARIANT:([A-Za-z0-9_]+)\s*-->\s*$")
STYLE_OPEN_RE = re.compile(r"^\s*<style\b[^>]*>\s*$", re.IGNORECASE)
STYLE_CLOSE_RE = re.compile(r"^\s*</style>\s*$", re.IGNORECASE)


def fail(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    print("Usage: python3 extract_variant.py <file> <variant>", file=sys.stderr)
    print("Example: python3 extract_variant.py hero-variants.html A", file=sys.stderr)
    print("Example: python3 extract_variant.py conversion-variants.html PRICING", file=sys.stderr)
    raise SystemExit(1)


def resolve_path(raw_path: str) -> Path:
    candidate = Path(raw_path).expanduser()
    if candidate.exists():
        return candidate.resolve()

    script_dir = Path(__file__).resolve().parent
    fallbacks = [
        script_dir.parent / "sections" / raw_path,
        script_dir / raw_path,
        Path.cwd() / raw_path,
    ]
    for fallback in fallbacks:
        if fallback.exists():
            return fallback.resolve()

    fail(f"file not found: {raw_path}")


def parse_segments(lines: list[str]) -> tuple[list[tuple[int, int]], list[dict[str, object]]]:
    style_blocks: list[tuple[int, int]] = []
    segments: list[dict[str, object]] = []
    inside_style = False
    style_block_id = -1
    current: dict[str, object] | None = None

    for idx, line in enumerate(lines):
        if STYLE_OPEN_RE.search(line):
            inside_style = True
            style_block_id += 1
            style_blocks.append((idx, -1))

        start_match = START_RE.match(line)
        if start_match:
            if current is not None:
                fail("nested variant markers are not supported")
            current = {
                "variant": start_match.group(1).upper(),
                "start_marker": idx,
                "content_start": idx + 1,
                "inside_style": inside_style,
                "style_block_id": style_block_id if inside_style else None,
            }
            continue

        end_match = END_RE.match(line)
        if end_match:
            if current is None:
                fail(f"unexpected closing marker for {end_match.group(1)}")
            if current["variant"] != end_match.group(1).upper():
                fail(
                    f"marker mismatch: expected {current['variant']} but found {end_match.group(1).upper()}"
                )
            current["end_marker"] = idx
            current["content_end"] = idx
            segments.append(current)
            current = None
            continue

        if STYLE_CLOSE_RE.search(line):
            if style_block_id < 0:
                fail("found </style> before <style>")
            start_idx, _ = style_blocks[style_block_id]
            style_blocks[style_block_id] = (start_idx, idx)
            inside_style = False

    if current is not None:
        fail(f"unterminated variant marker for {current['variant']}")

    unresolved = [block for block in style_blocks if block[1] == -1]
    if unresolved:
        fail("unterminated <style> block")

    return style_blocks, segments


def build_style_output(lines, style_blocks, segments, variant):
    outputs = []

    full_style_segments = [
        segment
        for segment in segments
        if segment["variant"] == variant
        and "<style" in "".join(lines[segment["content_start"]:segment["content_end"]])
    ]
    for segment in full_style_segments:
        content = "".join(lines[segment["content_start"]:segment["content_end"]]).strip()
        if content:
            outputs.append((int(segment["start_marker"]), content))

    style_segment_groups = {}
    for segment in segments:
        if segment["variant"] != variant:
            continue
        if not segment["inside_style"]:
            continue
        content = "".join(lines[segment["content_start"]:segment["content_end"]])
        if "<style" in content:
            continue
        style_segment_groups.setdefault(int(segment["style_block_id"]), []).append(segment)

    block_segments = {}
    for segment in segments:
        if segment["inside_style"] and segment["style_block_id"] is not None:
            block_segments.setdefault(int(segment["style_block_id"]), []).append(segment)

    for block_id in style_segment_groups:
        start_idx, end_idx = style_blocks[block_id]
        all_block_segments = block_segments.get(block_id, [])
        marker_lines = {int(segment["start_marker"]) for segment in all_block_segments} | {
            int(segment["end_marker"]) for segment in all_block_segments
        }
        occupied_lines = {}
        for segment in all_block_segments:
            for line_idx in range(int(segment["content_start"]), int(segment["content_end"])):
                occupied_lines[line_idx] = str(segment["variant"])

        rendered = []
        for line_idx in range(start_idx, end_idx + 1):
            if line_idx in marker_lines:
                continue
            owner = occupied_lines.get(line_idx)
            if owner is not None and owner != variant:
                continue
            rendered.append(lines[line_idx])

        content = "".join(rendered).strip()
        if content:
            outputs.append((start_idx, content))

    outputs.sort(key=lambda item: item[0])
    return outputs


def build_markup_output(lines, segments, variant):
    outputs = []
    for segment in segments:
        if segment["variant"] != variant:
            continue
        content = "".join(lines[segment["content_start"]:segment["content_end"]])
        stripped = content.strip()
        if not stripped:
            continue
        if STYLE_OPEN_RE.match(stripped.splitlines()[0]):
            continue
        if segment["inside_style"]:
            continue
        outputs.append((int(segment["start_marker"]), stripped))

    outputs.sort(key=lambda item: item[0])
    return outputs


def main():
    if len(sys.argv) != 3:
        fail("expected a file path and a variant name")

    file_path = resolve_path(sys.argv[1])
    variant = sys.argv[2].strip().upper()
    if not variant:
        fail("variant name cannot be empty")

    lines = file_path.read_text().splitlines(keepends=True)
    style_blocks, segments = parse_segments(lines)

    if not any(segment["variant"] == variant for segment in segments):
        fail(f"variant not found: {variant}")

    style_outputs = [content for _, content in build_style_output(lines, style_blocks, segments, variant)]
    markup_outputs = [content for _, content in build_markup_output(lines, segments, variant)]

    parts = [part for part in style_outputs + markup_outputs if part.strip()]
    if not parts:
        fail(f"no extractable content found for variant: {variant}")

    sys.stdout.write("\n\n".join(parts).rstrip() + "\n")


if __name__ == "__main__":
    main()
