---
name: architecture-drift-detector
description: Use when starting significant work, reviewing recent changes, planning refactors, or seeing commit bursts that may indicate structural drift.
---

# Output Marker

Display:
using skill: architecture-drift-detector

---

# Architecture Drift Detector

## Overview

Architecture usually degrades through clusters of broad changes. Detect risk
early and recommend focused architecture review without blocking routine work.

## Trigger Signals

Inspect recent repository activity when available. Recommend review when recent
changes include at least two of:

- Many files changed.
- Multiple packages or applications touched.
- Domain, data-access, runtime, or root configuration changed.
- Large line churn.
- Repeated fixes around the same boundary.

If history is unavailable, state that metadata is unknown and continue.

## Output When Triggered

Briefly report:

- What risk signal was observed.
- Which packages or boundaries appear affected.
- What focused review should happen before broad follow-up work.

Do not block small fixes, documentation-only work, dependency bumps, or test-only
changes unless they reveal structural coupling.

## Usage Checklist

- Recent changes were inspected when possible.
- Risk is tied to concrete files or package areas.
- Recommendation is proportionate and actionable.
- Routine work is not blocked by weak signals.

## Cross-References

- WITH: library-placement-decision, nx-module-boundaries
