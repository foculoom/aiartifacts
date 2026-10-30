#!/usr/bin/env python3
"""Flag selected prose for editorial review; never score or rewrite writing.

Only UTF-8 .md and .txt files are supported. Findings are review candidates,
not errors, evidence of AI authorship, or a judgment of literary quality.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from collections import defaultdict
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import re
import sys
from typing import Iterable, Mapping, Sequence


TERMS = (
    "tranche", "gate", "delve", "tapestry", "testament", "beacon",
    "revolutionize", "moreover", "furthermore",
)
STOCK_PHRASES = (
    "in today's fast-paced world", "it is worth noting",
    "in conclusion", "to summarize",
)
EXCLUDED_DIRS = frozenset({
    ".git", ".hg", ".svn", ".agents", ".codex", "node_modules",
    "venv", ".venv", "env", ".env", "build", "dist", "target", "out",
    ".next", ".nuxt", ".output", "coverage", "htmlcov", ".cache",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", ".tox",
})
WORD_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)*", re.UNICODE)
TERM_RE = re.compile(
    r"(?<!\w)(?:" + "|".join(TERMS) + r")(?!\w)", re.IGNORECASE
)
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*)$")
LIST_RE = re.compile(r"^ {0,3}(?:[-+*]|\d+[.)])[ \t]+")
REF_RE = re.compile(r"^ {0,3}\[([^\]\n]+)\]:[^\n]*(?:\n|$)", re.M)
URL_RE = re.compile(
    r"<[A-Za-z][A-Za-z0-9+.-]*:[^<>\s]*>"
    r"|\b(?:[A-Za-z][A-Za-z0-9+.-]*://|www\.)[^\s<>]+",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    rule: str
    excerpt: str


class LintError(Exception):
    """An input could not be read safely as a supported prose file."""


def _blank(text: str) -> str:
    """Remove content without moving original line/character positions."""
    return "".join("\n" if char == "\n" else " " for char in text)


def _normal(text: str) -> str:
    text = text.replace("’", "'")
    for dash in ("‐", "‑", "–"):
        text = text.replace(dash, "-")
    return " ".join(text.casefold().split())


def _excerpt(text: str) -> str:
    compact = " ".join(text.split())
    return compact if len(compact) <= 160 else compact[:157] + "..."


def _term_excerpt(text: str, match: re.Match) -> str:
    line_start = text.rfind("\n", 0, match.start()) + 1
    line_end = text.find("\n", match.end())
    if line_end < 0:
        line_end = len(text)
    left = max(line_start, match.start() - 65)
    right = min(line_end, match.end() + 75)
    excerpt = text[left:right]
    if left > line_start:
        excerpt = "..." + excerpt
    if right < line_end:
        excerpt += "..."
    return _excerpt(excerpt)


def _block_start(line: str) -> bool:
    return bool(
        HEADING_RE.match(line) or LIST_RE.match(line)
        or FENCE_RE.match(line)
        or re.match(r"^ {0,3}(?:\*\s*){3,}$|^ {0,3}(?:-\s*){3,}$"
                    r"|^ {0,3}(?:_\s*){3,}$", line.rstrip())
    )


def visible_prose(text: str) -> str:
    """Mask common Markdown non-prose while retaining source positions.

    This is a deliberately small scanner, not a full CommonMark parser.
    It handles fenced/inline code, front matter, comments, blockquotes
    (including ordinary lazy continuations), and link destinations.
    """
    if text.startswith("\ufeff"):
        text = " " + text[1:]
    lines = text.splitlines(keepends=True)
    if lines and lines[0].strip() == "---":
        stop = None
        for index in range(1, len(lines)):
            if lines[index].strip() in {"---", "..."}:
                stop = index + 1
                break
        # An unmatched opening may be an ordinary thematic break.
        if stop is not None:
            lines[:stop] = [_blank(line) for line in lines[:stop]]
    text = "".join(lines)
    chars = list(text)
    fence_char, fence_size = "", 0
    in_quote = False
    offset = 0
    for source_line in text.splitlines(keepends=True):
        stop = offset + len(source_line)
        line = "".join(chars[offset:stop])
        fence = FENCE_RE.match(line.rstrip("\r\n"))
        if fence_char:
            chars[offset:stop] = _blank(line)
            if (fence and fence[1][0] == fence_char
                    and len(fence[1]) >= fence_size
                    and not fence[2].strip()):
                fence_char, fence_size = "", 0
        elif re.match(r"^ {0,3}>", line):
            content = re.sub(r"^ {0,3}>[ \t]?", "", line)
            in_quote = bool(content.strip())
            chars[offset:stop] = _blank(line)
        elif in_quote and line.strip() and not _block_start(line):
            chars[offset:stop] = _blank(line)
        else:
            in_quote = False
            if fence and not (fence[1][0] == "`" and "`" in fence[2]):
                fence_char, fence_size = fence[1][0], len(fence[1])
                chars[offset:stop] = _blank(line)
            else:
                cursor = offset
                while cursor < stop:
                    if "".join(chars[cursor:cursor + 4]) == "<!--":
                        end = text.find("-->", cursor + 4)
                        end = len(text) if end < 0 else end + 3
                        chars[cursor:end] = _blank(text[cursor:end])
                        cursor = end
                    elif chars[cursor] == "`":
                        opening = re.match(r"`+", text[cursor:])[0]
                        back = cursor - 1
                        while back >= 0 and text[back] == "\\":
                            back -= 1
                        escaped = (cursor - back - 1) % 2 == 1
                        end = None
                        if not escaped:
                            for closing in re.finditer(
                                    r"`+", text[cursor + len(opening):]):
                                close_start = (cursor + len(opening)
                                               + closing.start())
                                between = text[cursor:close_start]
                                if re.search(r"\n[ \t]*\n", between):
                                    break
                                if len(closing[0]) == len(opening):
                                    end = close_start + len(closing[0])
                                    break
                        if end is not None:
                            chars[cursor:end] = _blank(text[cursor:end])
                            cursor = end
                        else:
                            cursor += len(opening)
                    else:
                        cursor += 1
        offset = stop
    text = "".join(chars)

    definitions = {_normal(match[1]) for match in REF_RE.finditer(text)}
    text = REF_RE.sub(lambda match: _blank(match[0]), text)
    chars = list(text)
    # Keep visible [labels]; mask balanced (...) destinations and titles.
    for opening in re.finditer(r"\]\(", text):
        start = opening.end() - 1
        if chars[start] == " ":
            continue
        depth, cursor, quote, angle = 1, start + 1, "", False
        while cursor < len(text) and depth:
            char = text[cursor]
            if char == "\\":
                cursor += 2
                continue
            if quote:
                if char == quote:
                    quote = ""
            elif angle:
                if char == ">":
                    angle = False
            elif char == "<":
                angle = True
            elif char in "\"'" and text[cursor - 1].isspace():
                quote = char
            elif char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            cursor += 1
        if depth == 0:
            chars[start:cursor] = _blank(text[start:cursor])
    text = "".join(chars)
    text = re.sub(
        r"(?<=\])\s*\[([^\]\n]*)\]",
        lambda match: _blank(match[0])
        if not match[1] or _normal(match[1]) in definitions else match[0],
        text,
    )
    return URL_RE.sub(lambda match: _blank(match[0]), text)


def _paragraphs(text: str) -> list[tuple[int, str]]:
    paragraphs = []
    pending = []
    first = 0

    def flush() -> None:
        if pending:
            paragraph = " ".join(pending)
            if len(WORD_RE.findall(paragraph)) >= 20:
                paragraphs.append((first, paragraph))
            pending.clear()

    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or HEADING_RE.match(line):
            flush()
            continue
        # Separate list entries instead of treating an entire list as prose.
        if LIST_RE.match(line):
            flush()
            line = LIST_RE.sub("", line, count=1)
        if not pending:
            first = number
        pending.append(line.strip())
    flush()
    return paragraphs


def lint_documents(
    documents: Mapping[str, str], *, allow_terms: Iterable[str] = (),
    check_heading_sequences: bool = False,
) -> list[Finding]:
    """Review in-memory path/text pairs, including cross-document repeats.

    Repeated paragraphs need at least 20 words and two distinct documents.
    Optional trailing H2 sequences need at least 4 headings in 3 documents.
    Allow terms suppress exact word/phrase rules only, not repetition rules.
    """
    allowed = {_normal(term) for term in allow_terms}
    findings = []
    paragraphs = defaultdict(list)
    suffixes = defaultdict(list)
    for path, original in sorted(documents.items()):
        text = visible_prose(original)
        starts = [0] + [m.end() for m in re.finditer("\n", text)]
        lines = text.splitlines()
        for match in TERM_RE.finditer(text):
            if _normal(match[0]) not in allowed:
                line = bisect_right(starts, match.start())
                findings.append(Finding(path, line, "word-choice",
                                        _term_excerpt(text, match)))
        for phrase in STOCK_PHRASES:
            if _normal(phrase) in allowed:
                continue
            pattern = r"\s+".join(re.escape(word)
                                     for word in phrase.split())
            pattern = pattern.replace("'", "['’]")
            pattern = pattern.replace(r"\-", "[-‐‑–]")
            for match in re.finditer(r"(?<!\w)" + pattern + r"(?!\w)",
                                     text, re.IGNORECASE):
                findings.append(Finding(
                    path, bisect_right(starts, match.start()),
                    "stock-phrase", _excerpt(match[0]),
                ))
        for line, paragraph in _paragraphs(text):
            paragraphs[_normal(paragraph)].append((path, line, paragraph))
        if check_heading_sequences:
            headings = []
            for number, line in enumerate(lines, 1):
                match = HEADING_RE.match(line)
                if match and match[1] == "##":
                    title = re.sub(r"\s+#+\s*$", "", match[2]).strip()
                    if title:
                        headings.append((number, _normal(title)))
            for length in range(4, len(headings) + 1):
                suffix = headings[-length:]
                suffixes[tuple(title for _, title in suffix)].append(
                    (path, suffix[0][0]))
    for copies in paragraphs.values():
        if len({path for path, _, _ in copies}) >= 2:
            findings.extend(Finding(path, line, "repeated-paragraph",
                                    _excerpt(paragraph))
                            for path, line, paragraph in copies)
    # Report only the longest qualifying suffix in each document.
    longest = {}
    for sequence, copies in suffixes.items():
        if len({path for path, _ in copies}) < 3:
            continue
        for path, line in copies:
            if path not in longest or len(sequence) > len(longest[path][1]):
                longest[path] = (line, sequence)
    findings.extend(Finding(path, line, "repeated-h2-sequence",
                            _excerpt(" → ".join(sequence)))
                    for path, (line, sequence) in longest.items())
    return sorted(set(findings), key=lambda item:
                  (item.path, item.line, item.rule, item.excerpt))


def _safe_absolute(path: Path) -> Path:
    absolute = path.expanduser().absolute()
    cursor = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        cursor /= part
        if cursor.is_symlink():
            raise LintError(f"Symlink input is not followed: {path}")
    return Path(os.path.abspath(absolute))


def collect_paths(inputs: Sequence[str | Path]) -> list[Path]:
    """Collect supported regular files; nested symlinks/artifacts are skipped."""
    found = set()

    def walk_error(error: OSError) -> None:
        raise LintError(str(error)) from error

    for raw in inputs:
        try:
            path = _safe_absolute(Path(raw))
            if not path.exists():
                raise LintError(f"Input does not exist: {raw}")
            if any(part.casefold() in EXCLUDED_DIRS for part in path.parts):
                continue
            if path.is_file():
                if path.suffix.lower() not in {".md", ".txt"}:
                    raise LintError(f"Unsupported input (use .md/.txt): {raw}")
                found.add(path)
            elif path.is_dir():
                for base, dirs, files in os.walk(path, followlinks=False,
                                                  onerror=walk_error):
                    dirs[:] = sorted(name for name in dirs
                                     if name.casefold() not in EXCLUDED_DIRS
                                     and not (Path(base) / name).is_symlink())
                    for name in sorted(files):
                        candidate = Path(base) / name
                        if (candidate.suffix.lower() in {".md", ".txt"}
                                and not candidate.is_symlink()
                                and candidate.is_file()):
                            found.add(candidate)
            else:
                raise LintError(f"Not a regular file or directory: {raw}")
        except OSError as error:
            raise LintError(f"Cannot inspect {raw}: {error}") from error
    return sorted(found, key=str)


def _read_documents(paths: Sequence[Path]) -> dict[str, str]:
    documents = {}
    for path in paths:
        try:
            documents[str(path)] = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as error:
            raise LintError(f"Cannot read {path}: {error}") from error
    return documents


def lint_paths(
    inputs: Sequence[str | Path], *, allow_terms: Iterable[str] = (),
    check_heading_sequences: bool = False,
) -> list[Finding]:
    """Read supported UTF-8 inputs, raising LintError for input/read errors."""
    return lint_documents(_read_documents(collect_paths(inputs)),
                          allow_terms=allow_terms,
                          check_heading_sequences=check_heading_sequences)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help=".md/.txt files or directories")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--allow-term", action="append", default=[],
                        help="allow an exact word or stock phrase; repeatable")
    parser.add_argument("--fail-on-findings", action="store_true",
                        help="exit 1 for findings instead of the default 0")
    parser.add_argument("--check-heading-sequences", action="store_true",
                        help="review repeated trailing H2 sequences")
    args = parser.parse_args(argv)
    try:
        paths = collect_paths(args.paths)
        findings = lint_documents(
            _read_documents(paths), allow_terms=args.allow_term,
            check_heading_sequences=args.check_heading_sequences)
    except LintError as error:
        print(f"prose_lint: {error}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps({"files_checked": len(paths),
                          "findings": [asdict(item) for item in findings]},
                         ensure_ascii=False, indent=2))
    elif findings:
        for finding in findings:
            print(f"{finding.path}:{finding.line}: {finding.rule}: "
                  f"{finding.excerpt}")
        print(f"{len(findings)} review candidate(s); editorial review required.")
    else:
        print("No findings from the selected checks; this is not a quality assessment.")
    return 1 if findings and args.fail_on_findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
