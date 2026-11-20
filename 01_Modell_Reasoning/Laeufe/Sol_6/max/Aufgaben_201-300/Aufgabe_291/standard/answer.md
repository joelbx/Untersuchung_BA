NVD CVSS v4.0 metrics now populate the existing `CveContent` score, vector, and severity fields by source. `Cvss40Scores()` returns available MITRE entries followed by NVD entries. The dependency was updated to a locally cached version that exposes NVD v4.0 metrics.

Conversion and aggregation tests were added. The `models`, `detector`, and `reporter` suites pass offline.