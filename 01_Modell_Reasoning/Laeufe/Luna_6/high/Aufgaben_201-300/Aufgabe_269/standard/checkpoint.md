# Checkpoint

Issue: Preserve Trivy vulnerability metadata separately for each advisory source.

Implemented source-specific Trivy content keys, per-source CVSS and vendor severity handling, publication timestamps, model aggregation, and TUI reference traversal. Both scan result conversion and library DB enrichment now keep source-specific records. Existing legacy `trivy` content remains visible in the TUI for old reports.

Validation: Focused tests passed for `contrib/trivy/pkg`, `models`, `detector`, and `tui`; running them again after final review edits.
