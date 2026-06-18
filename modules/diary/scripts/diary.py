#!/usr/bin/env python3
"""Append and inspect repo-local AI agent diary entries."""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Iterable, Iterator


REDACTIONS = (
    (
        re.compile(
            r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----",
            re.DOTALL,
        ),
        "[REDACTED PRIVATE KEY]",
    ),
    (
        re.compile(r"(?i)(authorization\s*:\s*)(?:bearer|basic)\s+[A-Za-z0-9._~+/\-=]+"),
        r"\1[REDACTED]",
    ),
    (
        re.compile(r"(?i)\b(bearer)\s+[A-Za-z0-9._~+/\-=]{16,}"),
        r"\1 [REDACTED]",
    ),
    (
        re.compile(
            r"(?i)\b([A-Z0-9_]*(?:API[_-]?KEY|SECRET|TOKEN|PASSWORD|PASSWD|PWD))\b"
            r"(\s*[:=]\s*)([\"']?)([^\s\"']+)([\"']?)"
        ),
        r"\1\2\3[REDACTED]\5",
    ),
    (
        re.compile(
            r"\b(?:sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9_]{20,}|"
            r"github_pat_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{20,})\b"
        ),
        "[REDACTED TOKEN]",
    ),
    (
        re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
        "[REDACTED JWT]",
    ),
)

ENTRY_START = re.compile(r"(?m)^## \d{2}:\d{2} - .*$")


def redact(value: str) -> str:
    """Redact common secret shapes from a string."""
    result = value
    for pattern, replacement in REDACTIONS:
        result = pattern.sub(replacement, result)
    return result


def clean(value: str | None) -> str:
    if value is None:
        return ""
    return redact(value.strip())


def clean_list(values: Iterable[str] | None) -> list[str]:
    if not values:
        return []

    cleaned: list[str] = []
    for value in values:
        item = clean(value)
        if item:
            cleaned.append(item)
    return cleaned


def resolve_root(repo: str | None) -> Path:
    base = Path(repo or os.getcwd()).expanduser().resolve()
    if repo is not None and not base.exists():
        raise ValueError(f"--repo does not exist: {base}")
    if base.is_file():
        base = base.parent

    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=base,
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return base

    stdout = result.stdout.strip()
    return Path(stdout).resolve() if stdout else base


def parse_now(raw_date: str | None) -> dt.datetime:
    now = dt.datetime.now().replace(microsecond=0)
    if not raw_date:
        return now

    try:
        day = dt.date.fromisoformat(raw_date)
    except ValueError as exc:
        raise ValueError("--date must use YYYY-MM-DD format") from exc

    return dt.datetime.combine(day, now.time())


@contextlib.contextmanager
def exclusive_lock(file_obj) -> Iterator[None]:
    try:
        import fcntl
    except ImportError:
        yield
        return

    fcntl.flock(file_obj.fileno(), fcntl.LOCK_EX)
    try:
        yield
    finally:
        fcntl.flock(file_obj.fileno(), fcntl.LOCK_UN)


def format_bullets(items: list[str], default: str | None = None) -> list[str]:
    if not items:
        if default is None:
            return []
        items = [default]

    lines: list[str] = []
    for item in items:
        parts = item.splitlines() or [""]
        first = parts[0]
        lines.append(f"- {first}" if first else "-")
        for line in parts[1:]:
            lines.append(f"  {line}")
    return lines


def add_section(
    lines: list[str],
    title: str,
    items: list[str],
    default: str | None = None,
) -> None:
    bullets = format_bullets(items, default)
    if not bullets:
        return

    lines.extend((f"### {title}", ""))
    lines.extend(bullets)
    lines.append("")


def build_entry(args: argparse.Namespace, now: dt.datetime) -> str:
    title = clean(args.title) or "Agent diary entry"
    source = clean(args.source) or "agent"
    cwd = redact(str(Path.cwd().resolve()))

    lines = [
        f"## {now:%H:%M} - {title}",
        "",
        f"Source: {source}",
        f"Working directory: {cwd}",
        "",
    ]

    add_section(lines, "Summary", clean_list(args.summary), "No summary provided.")
    add_section(lines, "Actions", clean_list(args.action))
    add_section(lines, "Decisions", clean_list(args.decision))
    add_section(lines, "Done", clean_list(args.done))
    add_section(lines, "Validation", clean_list(args.validation))
    add_section(lines, "Blockers", clean_list(args.blocker), "None")
    add_section(lines, "Changed Files", clean_list(args.file))
    add_section(lines, "Next", clean_list(args.next), "None")

    return "\n".join(lines).rstrip() + "\n"


def diary_path(root: Path, now: dt.datetime) -> Path:
    return root / ".diary" / f"{now:%Y-%m-%d}.md"


def append_entry(path: Path, now: dt.datetime, entry: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a+", encoding="utf-8") as handle:
        with exclusive_lock(handle):
            handle.seek(0)
            existing = handle.read()
            handle.seek(0, os.SEEK_END)

            if not existing:
                handle.write(f"# {now:%Y-%m-%d}\n\n")
            else:
                if not existing.endswith("\n"):
                    handle.write("\n")
                if not existing.endswith("\n\n"):
                    handle.write("\n")

            handle.write(entry.rstrip() + "\n")
            handle.flush()
            os.fsync(handle.fileno())


def print_preview(path: Path, entry: str) -> None:
    print(f"# Diary path: {path}")
    print()
    print(entry, end="")


def command_append(args: argparse.Namespace) -> int:
    try:
        root = resolve_root(args.repo)
        now = parse_now(args.date)
    except ValueError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2

    entry = build_entry(args, now)
    path = diary_path(root, now)

    if args.dry_run:
        print_preview(path, entry)
        return 0

    try:
        append_entry(path, now, entry)
    except OSError as exc:
        print(f"[ERROR] Could not write diary entry: {exc}", file=sys.stderr)
        print("\nWould-be diary entry:\n", file=sys.stderr)
        print(entry, file=sys.stderr)
        return 1

    print(path)
    return 0


def command_dry_run(args: argparse.Namespace) -> int:
    args.dry_run = True
    return command_append(args)


def split_entries(text: str) -> list[str]:
    matches = list(ENTRY_START.finditer(text))
    entries: list[str] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        entry = text[start:end].strip()
        if entry:
            entries.append(entry)
    return entries


def command_recent(args: argparse.Namespace) -> int:
    try:
        root = resolve_root(args.repo)
    except ValueError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2

    diary_dir = root / ".diary"

    if not diary_dir.exists():
        print(f"No diary entries found in {diary_dir}")
        return 0

    collected: list[tuple[Path, str]] = []
    for path in sorted(diary_dir.glob("*.md"), key=lambda item: item.name, reverse=True):
        try:
            entries = split_entries(path.read_text(encoding="utf-8"))
        except OSError as exc:
            print(f"[WARN] Could not read {path}: {exc}", file=sys.stderr)
            continue

        for entry in reversed(entries):
            collected.append((path, entry))
            if len(collected) >= args.limit:
                break
        if len(collected) >= args.limit:
            break

    if not collected:
        print(f"No diary entries found in {diary_dir}")
        return 0

    for index, (path, entry) in enumerate(collected):
        if index:
            print("\n---\n")
        try:
            label = path.relative_to(root)
        except ValueError:
            label = path
        print(f"<!-- {label} -->")
        print(entry)

    return 0


def add_entry_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo", help="Directory used to resolve the project root.")
    parser.add_argument("--date", help="Entry date in YYYY-MM-DD format. Defaults to today.")
    parser.add_argument("--source", default="agent", help="Agent or tool writing the entry.")
    parser.add_argument("--title", required=True, help="Short entry title.")
    parser.add_argument(
        "--summary",
        action="append",
        required=True,
        help="Concise summary bullet. Repeat for multiple bullets.",
    )
    parser.add_argument("--action", action="append", default=[], help="Important action bullet.")
    parser.add_argument("--decision", action="append", default=[], help="Decision and reason bullet.")
    parser.add_argument("--done", action="append", default=[], help="Completed outcome bullet.")
    parser.add_argument("--validation", action="append", default=[], help="Validation result bullet.")
    parser.add_argument("--blocker", action="append", default=[], help="Blocker bullet.")
    parser.add_argument("--file", action="append", default=[], help="Changed or important file path.")
    parser.add_argument("--next", action="append", default=[], help="Follow-up bullet.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    append_parser = subparsers.add_parser("append", help="Append a diary entry.")
    add_entry_arguments(append_parser)
    append_parser.add_argument("--dry-run", action="store_true", help="Print without writing.")
    append_parser.set_defaults(func=command_append)

    dry_run_parser = subparsers.add_parser("dry-run", help="Preview a diary entry without writing.")
    add_entry_arguments(dry_run_parser)
    dry_run_parser.set_defaults(func=command_dry_run)

    recent_parser = subparsers.add_parser("recent", help="Show recent diary entries.")
    recent_parser.add_argument("--repo", help="Directory used to resolve the project root.")
    recent_parser.add_argument(
        "--limit",
        type=int,
        default=3,
        help="Maximum number of entries to show.",
    )
    recent_parser.set_defaults(func=command_recent)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if getattr(args, "limit", 1) < 1:
        print("[ERROR] --limit must be at least 1", file=sys.stderr)
        return 2

    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
