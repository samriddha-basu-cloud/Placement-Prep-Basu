#!/usr/bin/env python3
"""Build index.html: embeds every markdown note from ./notes into src/template.html.

Usage:  python3 build.py
No third-party packages needed. Re-run whenever you edit a note or the template.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
NOTES = ROOT / "notes"
TEMPLATE = ROOT / "src" / "template.html"
OUT = ROOT / "index.html"
SKIP_DIRS = {"_Templates", ".obsidian", ".trash"}


def collect():
    notes = []
    for p in sorted(NOTES.rglob("*.md")):
        rel = p.relative_to(NOTES)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        folder = rel.parent.as_posix() if len(rel.parts) > 1 else ""
        notes.append({"id": p.stem, "folder": folder, "md": p.read_text(encoding="utf-8")})
    ids = [n["id"] for n in notes]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        sys.exit(f"Duplicate note names (wikilinks need unique names): {sorted(dupes)}")
    return notes


def main():
    notes = collect()
    data = json.dumps(notes, ensure_ascii=False, separators=(",", ":"))
    # keep the JSON safe inside a <script> element
    data = data.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    html = TEMPLATE.read_text(encoding="utf-8")
    if "__NOTES_JSON__" not in html:
        sys.exit("placeholder __NOTES_JSON__ missing from template")
    html = html.replace("__NOTES_JSON__", data)
    OUT.write_text(html, encoding="utf-8")
    print(f"Built {OUT.name}: {len(notes)} notes, {OUT.stat().st_size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    main()
