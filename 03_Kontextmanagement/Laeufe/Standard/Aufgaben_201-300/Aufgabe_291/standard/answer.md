NVD CVSS v4.0 metrics are now converted into `CveContent` with their source and included in `Cvss40Scores()` after MITRE entries. The three v4.0 model fields already existed; I updated `go-cve-dictionary` to a locally cached version that exposes `Nvd.Cvss40` and added regression tests.

The focused tests and full `models` suite pass. The detector suite produced no result before I interrupted it.