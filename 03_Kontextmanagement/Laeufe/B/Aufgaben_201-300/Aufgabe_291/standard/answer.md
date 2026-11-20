I updated NVD conversion to map CVSS v4.0 metrics by source when the field is available, and `Cvss40Scores()` now returns MITRE entries before NVD entries. `go test ./models` passes offline.

**The issue is not fully resolved with the pinned dependency:** its `Nvd` type has no `Cvss40` field, so it cannot supply NVD v4.0 values to the converter.