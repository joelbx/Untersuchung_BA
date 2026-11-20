# Checkpoint

Task: preserve Trivy CVE data by source across conversion, library detection, model aggregation, and TUI references.

Status: investigating root cause before edits. Working tree initially clean. `rg` is unavailable (`/bin/bash: rg: command not found`); using `find`/`grep`.

Root cause: `Convert` replaces `CveContents` for each target and writes only `models.Trivy`; `getCveContents` also writes only `models.Trivy`. Both discard `VendorSeverity` and `CVSS` source maps. Model score readers enumerate fixed types without Trivy source keys, and TUI explicitly reads only `models.Trivy`. Local Trivy types confirm `VendorSeverity map[SourceID]Severity`, `CVSS map[SourceID]CVSS`, and dates on `Vulnerability`.

Hypothesis: building one content per union of severity/CVSS source IDs, merging it by source across targets, then enumerating those types will retain distinct source metadata.

Implementation: added Trivy source type constants and source enumeration; shared builder in models/trivy.go creates one content per severity/CVSS source and preserves identity, scores, vectors, references, and dates. Converter merges sources across targets. Library detector uses the builder and merges newly found source entries into existing CVEs. Model aggregation and TUI enumerate Trivy source types.

Regression: `go test -mod=readonly ./contrib/trivy/pkg -run TestConvertPreservesTrivySourcesAcrossTargets -count=1` failed before the fix because `trivy:debian`, `trivy:nvd`, and `trivy:ubuntu` were missing. Added library and aggregation tests.

Verification: `go test -mod=readonly ./contrib/trivy/pkg ./models ./detector ./tui` passed (TUI has no test files). `git diff --check` passed. An earlier broad test run was interrupted while compiling dependencies after a replacement run started; the replacement completed successfully.
