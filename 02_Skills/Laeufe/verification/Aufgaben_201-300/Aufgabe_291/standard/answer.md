NVD CVSS v4.0 metrics are now converted into `CveContent` by metric source and included in `Cvss40Scores()` after MITRE entries. The existing `CveContent` v4.0 fields were already present; I updated the dependency pin to a locally cached version that provides `Nvd.Cvss40`.

Focused tests and the full `models` and `detector` package tests passed with network access disabled.