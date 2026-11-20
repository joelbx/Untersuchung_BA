# Checkpoint: multi-format rule segments

- Goal complete: rule configuration accepts string segments and `{keys, operator}` objects across import/export, filesystem snapshots, and SQL persistence.
- Implementation: added `SegmentEmbed`, `SegmentKey`, `Segments`, strict YAML format/field validation, and OR normalization for one-key segments; adapted importer/exporter and snapshot handling; normalized single-key rule and rollout operators in SQL common persistence; updated requested YAML fixtures, exporter fixture data, and the supplied multi-segment import fixture.
- Verification passed: `go test ./internal/ext ./internal/storage/fs ./internal/storage/sql`; `go test ./internal/storage/sql/...`; `git diff --check`.
- Constraints followed: local repository code and existing tests only; no git history, index baseline, or harness configuration changes.
