#!/usr/bin/env python3
"""Audit recent Codex prompts against routed skill metadata without writing files."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
REBUILD_PATH = SCRIPT_DIR / 'rebuild-routed-skills.py'
DEFAULT_HISTORY = Path.home() / '.codex' / 'history.jsonl'
DEFAULT_LOGS = Path.home() / '.codex' / 'logs_2.sqlite'

EXPECTED_TERMS = {
    'design-intake': (
        'unclear',
        'understand what i want',
        'what i want to do',
        'goal',
        'scope',
        'success criteria',
    ),
    'grill-with-docs': (
        'grill',
        'challenge',
        'ask me',
        'ask questions',
        'go deeper',
        'deeper',
    ),
    'implementation-plan': (
        'draft a plan',
        'full plan',
        'phases',
        'plan to',
        'roadmap',
    ),
    'issue-decomposition': (
        'huge plan',
        'multiple detailed phases',
        'vertical slices',
        'briefs',
    ),
    'plan-execution': (
        'implement this plan',
        'implement the plan',
        'execute the plan',
        '/goal',
    ),
    'review-gate': (
        'review',
        'audit',
        'findings',
        'quality',
        'code smell',
    ),
    'skill-evolution': (
        'routing',
        'router',
        'facets',
        'module facets',
        'repeated agent failure',
        'workspace conventions',
    ),
    'workspace-state-guard': (
        'dirty tree',
        'current changes',
        'substantial edits',
        'cleanup',
    ),
    'branch-completion': (
        'commit',
        'push',
        'pull request',
        'merge',
    ),
    'test-first-discipline': (
        'test',
        'vitest',
        'playwright',
        'e2e',
        'bug',
        'regression',
    ),
    'playwright-conventions': (
        'playwright',
        'e2e',
        'browser project',
        'locator',
    ),
    'vitest-conventions': (
        'vitest',
        'vi.fn',
        'vi.mock',
    ),
    'no-transitional-architecture': (
        'shim',
        'stub',
        'temporary',
        'legacy',
        'implementation layer',
        'transitional',
    ),
    'library-placement-decision': (
        'libraries/',
        'libs/',
        'new library',
        'shared code',
        'where',
    ),
    'nx-conventions': (
        'nx',
        'project.json',
        'nx.json',
        'executor',
        'generate',
    ),
    'nx-module-boundaries': (
        'apps/',
        'libs/',
        'boundaries',
        'node library',
        'browser',
    ),
    'public-api-design': (
        'public api',
        'export',
        'contract',
        'sdk',
        'abstracts',
    ),
    'naming-consistency': (
        'naming',
        'names',
        'rename',
    ),
    'typescript-api-conventions': (
        'types',
        'interface',
        'abstracts',
        'contract',
        'dto',
        'generic',
    ),
    'typescript-code-style': (
        'typescript',
        'strict',
        'class',
        'function',
    ),
    'code-documentation': (
        'documentation',
        'docs',
        'jsdoc',
        'tsdoc',
        'implement',
        'refactor',
    ),
    'completion-verification': (
        'done',
        'complete',
        'validation proof',
        'acceptance',
    ),
}


@dataclass(frozen=True)
class Prompt:
    """One user prompt from Codex history."""

    ts: int
    session_id: str
    text: str


def load_rebuild_module() -> Any:
    """Load the sibling rebuild helper without requiring package installation."""
    spec = importlib.util.spec_from_file_location('rebuild_routed_skills', REBUILD_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f'cannot load {REBUILD_PATH}')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def normalize_text(value: str) -> str:
    """Collapse whitespace for matching and display."""
    return ' '.join(value.split())


def parse_since(value: str | None) -> int | None:
    """Parse an ISO date or datetime into a Unix timestamp."""
    if not value:
        return None
    parsed = dt.datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return int(parsed.timestamp())


def load_history(path: Path) -> list[Prompt]:
    """Load Codex history JSONL prompts."""
    prompts: list[Prompt] = []
    if not path.exists():
        return prompts
    for line in path.read_text(encoding='utf-8').splitlines():
        try:
            raw = json.loads(line)
        except json.JSONDecodeError:
            continue
        text = raw.get('text')
        if not isinstance(text, str):
            continue
        prompts.append(
            Prompt(
                ts=int(raw.get('ts') or 0),
                session_id=str(raw.get('session_id') or ''),
                text=normalize_text(text),
            )
        )
    return prompts


def cortex_prompts(prompts: list[Prompt], since: int | None, recent: int) -> list[Prompt]:
    """Return recent prompts that explicitly reference Cortex routing."""
    filtered = [
        prompt for prompt in prompts
        if (since is None or prompt.ts >= since)
        and ('$cortex' in prompt.text.lower() or 'cortex' in prompt.text.lower())
    ]
    if recent > 0:
        return filtered[-recent:]
    return filtered


def module_facet_text(workspace: Any) -> dict[str, str]:
    """Return searchable facet text by active routed module name."""
    result: dict[str, str] = {}
    for artifact in workspace.modules:
        if artifact.activation != 'routed' or artifact.status != 'active':
            continue
        values: list[str] = []
        for key in workspace.facet_keys:
            values.extend(artifact.facets.get(key, []))
        result[artifact.name] = normalize_text(' '.join(values)).lower()
    return result


def matched_terms(prompts: list[Prompt], modules: dict[str, str]) -> dict[str, dict[str, Any]]:
    """Compare recent prompt language with current routing facet language."""
    report: dict[str, dict[str, Any]] = {}
    prompt_text = '\n'.join(prompt.text.lower() for prompt in prompts)
    for module, terms in EXPECTED_TERMS.items():
        if module not in modules:
            continue
        found = sorted(term for term in terms if term in prompt_text)
        if not found:
            continue
        missing = sorted(term for term in found if term not in modules[module])
        report[module] = {
            'matched_terms': found,
            'missing_from_facets': missing,
            'matched_prompt_count': sum(1 for prompt in prompts if any(term in prompt.text.lower() for term in found)),
        }
    return report


def static_facet_risks(workspace: Any) -> list[dict[str, Any]]:
    """Identify metadata patterns that commonly weaken facet routing quality."""
    risks: list[dict[str, Any]] = []
    active = [
        artifact for artifact in workspace.modules
        if artifact.activation == 'routed' and artifact.status == 'active'
    ]
    for artifact in active:
        normalized_name = artifact.name.replace('-', ' ')
        if not artifact.lifecycle:
            risks.append({'module': artifact.name, 'risk': 'active module has no lifecycle files', 'detail': 'lifecycle'})
        for key, values in artifact.facets.items():
            for value in values:
                normalized_value = value.strip().lower().replace('-', ' ')
                if normalized_value == normalized_name:
                    risks.append({'module': artifact.name, 'risk': 'facet only restates module name', 'detail': f'{key}: {value}'})
                if 'evidence for ' in value.lower():
                    risks.append({'module': artifact.name, 'risk': 'facet uses mechanical evidence wording', 'detail': f'{key}: {value}'})
    return risks


def logs_summary(path: Path) -> dict[str, Any]:
    """Return a small optional summary of local Codex log availability."""
    if not path.exists():
        return {'available': False, 'marker_rows': 0}
    try:
        con = sqlite3.connect(path)
        marker_rows = con.execute(
            "select count(*) from logs where feedback_log_body like '%using module:%' "
            "or feedback_log_body like '%using skill:%'"
        ).fetchone()[0]
    except sqlite3.Error:
        return {'available': False, 'marker_rows': 0}
    return {'available': True, 'marker_rows': int(marker_rows)}


def render_text(report: dict[str, Any]) -> str:
    """Render a human-readable stdout audit report."""
    lines = [
        '# Routed History Audit',
        '',
        f"History prompts analyzed: {report['history_prompt_count']}",
        f"Cortex prompts analyzed: {report['cortex_prompt_count']}",
        f"Optional log DB available: {report['logs']['available']} ({report['logs']['marker_rows']} marker rows)",
        '',
        '## Likely Under-Faceted Modules',
    ]
    if report['term_matches']:
        for module, data in sorted(report['term_matches'].items()):
            missing = ', '.join(data['missing_from_facets']) or 'none'
            matched = ', '.join(data['matched_terms'])
            lines.append(f"- {module}: matched {data['matched_prompt_count']} prompts; missing facet terms: {missing}; matched terms: {matched}")
    else:
        lines.append('- none')
    lines.extend(['', '## Static Facet Risks'])
    if report['static_risks']:
        for risk in report['static_risks']:
            lines.append(f"- {risk['module']}: {risk['risk']} ({risk['detail']})")
    else:
        lines.append('- none')
    return '\n'.join(lines)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', default='routed-skills.yaml', help='Path to routed-skills.yaml.')
    parser.add_argument('--history', type=Path, default=DEFAULT_HISTORY, help='Path to Codex history JSONL.')
    parser.add_argument('--logs', type=Path, default=DEFAULT_LOGS, help='Optional Codex logs SQLite path.')
    parser.add_argument('--recent', type=int, default=50, help='Number of recent Cortex prompts to analyze; 0 means all.')
    parser.add_argument('--since', help='ISO date or datetime lower bound for history prompts.')
    parser.add_argument('--format', choices=('text', 'json'), default='text', help='Output format.')
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the stdout-only routing history audit."""
    args = parse_args(argv)
    rebuild = load_rebuild_module()
    workspace = rebuild.load_workspace(args.workspace)
    history = load_history(args.history)
    prompts = cortex_prompts(history, parse_since(args.since), args.recent)
    report = {
        'history_prompt_count': len(history),
        'cortex_prompt_count': len(prompts),
        'term_matches': matched_terms(prompts, module_facet_text(workspace)),
        'static_risks': static_facet_risks(workspace),
        'logs': logs_summary(args.logs),
    }
    if args.format == 'json':
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(render_text(report))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
