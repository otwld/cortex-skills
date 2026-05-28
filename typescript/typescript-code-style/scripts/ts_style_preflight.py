#!/usr/bin/env python3
"""Conservative Google-style TypeScript preflight checks.

This script catches mechanical issues that are high signal without needing a
TypeScript parser. It is not a formatter, typechecker, linter, or full style
validator.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
from dataclasses import dataclass
from typing import Iterable


TS_EXTENSIONS = {".ts", ".tsx", ".mts", ".cts"}
SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "node_modules",
    "bower_components",
    "dist",
    "build",
    "coverage",
    ".next",
    ".nuxt",
    ".turbo",
    ".cache",
}


@dataclass(frozen=True)
class Rule:
    code: str
    message: str
    pattern: re.Pattern[str]


CODE_RULES = [
    Rule("no-var", "Use const or let, never var.", re.compile(r"\bvar\s+[A-Za-z_$]")),
    Rule("no-default-export", "Use named exports in owned TypeScript.", re.compile(r"\bexport\s+default\b")),
    Rule("no-export-let", "Do not export mutable bindings; expose a getter or final const.", re.compile(r"\bexport\s+let\b")),
    Rule("no-namespace", "Use ES modules instead of namespace/module declarations.", re.compile(r"^\s*(export\s+)?(namespace|module)\s+[A-Za-z_$]", re.MULTILINE)),
    Rule("no-require-import", "Use ES module imports, not import = require().", re.compile(r"\bimport\s+\w+\s*=\s*require\s*\(")),
    Rule("no-require-call", "Use ES module imports, not require() calls.", re.compile(r"(?<![\w.])require\s*\(")),
    Rule("no-const-enum", "Use enum, not const enum.", re.compile(r"\bconst\s+enum\b")),
    Rule("no-debugger", "Remove debugger statements from production code.", re.compile(r"(?<![\w$])debugger\s*;")),
    Rule("no-eval", "Do not use eval().", re.compile(r"(?<![\w.])eval\s*\(")),
    Rule("no-function-constructor", "Do not construct functions from strings.", re.compile(r"\bnew\s+Function\s*\(")),
    Rule("no-with", "Do not use with statements.", re.compile(r"(?<![\w$])with\s*\(")),
    Rule("no-wrapper-constructors", "Do not instantiate String, Boolean, or Number wrappers.", re.compile(r"\bnew\s+(String|Boolean|Number)\s*\(")),
    Rule("no-array-constructor", "Use array literals or Array.from instead of Array constructors.", re.compile(r"(?<![\w.])(?:new\s+)?Array\s*\(")),
    Rule("no-object-constructor", "Use object literals instead of Object constructors.", re.compile(r"(?<![\w.])(?:new\s+)?Object\s*\(")),
    Rule("no-private-identifiers", "Use TypeScript private/protected instead of #private fields.", re.compile(r"(^|[^\w$])#[A-Za-z_$][\w$]*")),
    Rule("no-angle-type-assertion", "Use `as Type` assertions, not angle-bracket assertions.", re.compile(r"<[A-Z][A-Za-z0-9_.$]*(?:<[^;\n]+>)?>\s*[A-Za-z_$({[]")),
]

RAW_RULES = [
    Rule("no-triple-slash-reference", "Do not use triple-slash references in source files.", re.compile(r"///\s*<reference\b")),
    Rule("no-ts-directive", "Avoid @ts-ignore, @ts-expect-error, and @ts-nocheck.", re.compile(r"@ts-(ignore|expect-error|nocheck)\b")),
    Rule("no-legacy-octal-escape", "Use named or Unicode escapes, never legacy octal escapes.", re.compile(r"\\[1-7][0-7]{0,2}")),
]


@dataclass
class Finding:
    path: pathlib.Path
    line: int
    column: int
    code: str
    message: str
    text: str


def iter_files(paths: Iterable[pathlib.Path]) -> Iterable[pathlib.Path]:
    for path in paths:
        if not path.exists():
            continue
        if path.is_file() and path.suffix in TS_EXTENSIONS:
            yield path
            continue
        if path.is_dir():
            for child in path.rglob("*"):
                if child.is_dir():
                    continue
                if child.suffix not in TS_EXTENSIONS:
                    continue
                if any(part in SKIP_DIRS for part in child.parts):
                    continue
                yield child


def line_col(text: str, index: int) -> tuple[int, int]:
    line = text.count("\n", 0, index) + 1
    last_newline = text.rfind("\n", 0, index)
    column = index + 1 if last_newline == -1 else index - last_newline
    return line, column


def line_text(text: str, line: int) -> str:
    lines = text.splitlines()
    if 1 <= line <= len(lines):
        return lines[line - 1].strip()
    return ""


def mask_comments_and_strings(text: str) -> str:
    """Replace comments and string bodies with spaces while preserving offsets."""
    chars = list(text)
    i = 0
    n = len(chars)
    state = "code"
    quote = ""

    while i < n:
        char = chars[i]
        nxt = chars[i + 1] if i + 1 < n else ""

        if state == "code":
            if char == "/" and nxt == "/":
                chars[i] = chars[i + 1] = " "
                i += 2
                state = "line_comment"
                continue
            if char == "/" and nxt == "*":
                chars[i] = chars[i + 1] = " "
                i += 2
                state = "block_comment"
                continue
            if char in {"'", '"', "`"}:
                quote = char
                chars[i] = " "
                i += 1
                state = "string"
                continue
            i += 1
            continue

        if state == "line_comment":
            if char == "\n":
                state = "code"
            else:
                chars[i] = " "
            i += 1
            continue

        if state == "block_comment":
            if char == "*" and nxt == "/":
                chars[i] = chars[i + 1] = " "
                i += 2
                state = "code"
                continue
            if char != "\n":
                chars[i] = " "
            i += 1
            continue

        if state == "string":
            if char == "\\":
                chars[i] = " "
                if i + 1 < n and chars[i + 1] != "\n":
                    chars[i + 1] = " "
                    i += 2
                    continue
            elif char == quote:
                chars[i] = " "
                i += 1
                state = "code"
                continue
            elif char != "\n":
                chars[i] = " "
            i += 1
            continue

    return "".join(chars)


def check_file(path: pathlib.Path) -> list[Finding]:
    findings: list[Finding] = []

    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        findings.append(Finding(path, exc.start + 1, 1, "utf-8", "File is not valid UTF-8.", ""))
        return findings

    for index, char in enumerate(text):
        if char == "\t":
            line, column = line_col(text, index)
            findings.append(Finding(path, line, column, "no-tabs", "Use spaces, not tab characters.", line_text(text, line)))
        elif char.isspace() and char not in {" ", "\n", "\r"}:
            line, column = line_col(text, index)
            findings.append(Finding(path, line, column, "no-unicode-whitespace", "Escape or remove non-ASCII whitespace.", line_text(text, line)))

    code_text = mask_comments_and_strings(text)

    for rule in CODE_RULES:
        for match in rule.pattern.finditer(code_text):
            line, column = line_col(text, match.start())
            findings.append(Finding(path, line, column, rule.code, rule.message, line_text(text, line)))

    for rule in RAW_RULES:
        for match in rule.pattern.finditer(text):
            line, column = line_col(text, match.start())
            findings.append(Finding(path, line, column, rule.code, rule.message, line_text(text, line)))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Run conservative TypeScript style preflight checks.")
    parser.add_argument("paths", nargs="+", type=pathlib.Path, help="TypeScript files or directories to scan")
    parser.add_argument("--format", choices=("text", "jsonl"), default="text", help="Output format")
    args = parser.parse_args()

    files = sorted(set(iter_files(args.paths)))
    if not files:
        print("No TypeScript files found.", file=sys.stderr)
        return 0

    findings: list[Finding] = []
    for path in files:
        findings.extend(check_file(path))

    if args.format == "jsonl":
        import json

        for finding in findings:
            print(json.dumps({
                "path": str(finding.path),
                "line": finding.line,
                "column": finding.column,
                "code": finding.code,
                "message": finding.message,
                "text": finding.text,
            }, sort_keys=True))
    else:
        for finding in findings:
            print(f"{finding.path}:{finding.line}:{finding.column}: {finding.code}: {finding.message}")
            if finding.text:
                print(f"  {finding.text}")

    if findings:
        print(f"\n{len(findings)} finding(s) across {len(files)} file(s).", file=sys.stderr)
        return 1

    print(f"No preflight findings across {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
