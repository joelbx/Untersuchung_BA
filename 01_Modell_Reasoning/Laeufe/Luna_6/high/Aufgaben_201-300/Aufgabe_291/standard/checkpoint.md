# Checkpoint

Issue: Persist and expose CVSS v4.0 metrics from MITRE and NVD.

Changes:
- Confirmed `CveContent` already contains `Cvss40Score`, `Cvss40Vector`, and `Cvss40Severity`.
- Updated NVD conversion to group CVSS v4.0 metrics by metric source and copy score, vector, and severity into the corresponding NVD content.
- Updated score aggregation to enumerate MITRE then NVD.
- Updated `go-cve-dictionary` to the locally cached revision that exposes `Nvd.Cvss40`; no download was needed.

Verification: `GOPROXY=off go test ./models` passed.
