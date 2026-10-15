#!/usr/bin/env python3
"""The 16 READMEs stay in step.

    python3 scripts/check_readmes.py

README.md (English) and README.<locale>.md for the 15 other product locales must all exist, start with the same logo
block (the leading centred <picture> block), carry a language navigation line with 16 entries, and contain the same
set of URLs and the same fenced code blocks as README.md (whitespace-normalised). Prose may differ; commands, links and
the install sentence may not.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOCALES = ["pt", "es", "hi", "id", "vi", "th", "zh-CN", "zh-TW", "ja", "ko", "fil", "ru", "fr", "de", "tr"]
URL = re.compile(r"https?://[^\s<>()\[\]\"'`]+")
FENCE = re.compile(r"```[^\n]*\n(.*?)```", re.S)


def nav_index(lines: list[str]) -> int:
    """The language navigation line: the first line linking (almost) every README.<locale>.md."""
    for i, line in enumerate(lines):
        if line.count("README.") >= 12:
            return i
    return -1


def nav_entries(line: str) -> int:
    return len([p for p in re.split(r"\s[·|•]\s|\s\|\s", line.strip()) if p.strip()])


def logo_block(lines: list[str]) -> list[str]:
    """The leading centred <picture> block, up to and including its closing </p>."""
    for i, line in enumerate(lines):
        if line.strip() == "</p>":
            return lines[: i + 1]
    return []


def urls(text: str) -> set[str]:
    return {u.rstrip(".,;:") for u in URL.findall(text)}


def blocks(text: str) -> list[str]:
    return sorted("\n".join(l.strip() for l in b.strip().splitlines() if l.strip()) for b in FENCE.findall(text))


def main() -> None:
    errors: list[str] = []
    base = ROOT / "README.md"
    if not base.exists():
        sys.exit("README.md missing")
    en = base.read_text(encoding="utf-8")
    en_lines = en.splitlines()
    en_nav = nav_index(en_lines)
    if en_nav < 0:
        errors.append("README.md: no language navigation line")
    else:
        n = nav_entries(en_lines[en_nav])
        if n != 16:
            errors.append(f"README.md: navigation line has {n} entries, expected 16")
    logo = logo_block(en_lines)
    if not logo or "<picture>" not in "".join(logo):
        errors.append("README.md: no leading logo block (<p align=\"center\"> … <picture> … </p>)")
    en_urls, en_blocks = urls(en), blocks(en)

    for loc in LOCALES:
        p = ROOT / f"README.{loc}.md"
        if not p.exists():
            errors.append(f"README.{loc}.md: missing")
            continue
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()
        nav = nav_index(lines)
        if nav < 0:
            errors.append(f"README.{loc}.md: no language navigation line")
        else:
            n = nav_entries(lines[nav])
            if n != 16:
                errors.append(f"README.{loc}.md: navigation line has {n} entries, expected 16")
        if logo_block(lines) != logo:
            errors.append(f"README.{loc}.md: logo block differs from README.md")
        missing, extra = en_urls - urls(text), urls(text) - en_urls
        if missing:
            errors.append(f"README.{loc}.md: missing URLs {sorted(missing)}")
        if extra:
            errors.append(f"README.{loc}.md: extra URLs {sorted(extra)}")
        if blocks(text) != en_blocks:
            errors.append(f"README.{loc}.md: fenced code blocks differ from README.md ({len(blocks(text))} vs {len(en_blocks)})")
    for e in errors:
        print(e)
    if errors:
        sys.exit(f"{len(errors)} problem(s)")
    print(f"ok: README.md + {len(LOCALES)} locales agree")


if __name__ == "__main__":
    main()
