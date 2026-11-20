NVD CVSS v4.0 metrics are now parsed into `CveContent` by metric source, and `Cvss40Scores()` returns available MITRE entries followed by NVD entries. The three model fields already existed; I updated the pinned `go-cve-dictionary` version because the previous version lacked `Nvd.Cvss40`.

Tests passed: `go test ./models -count=1` and a reporter package compile check. No delegation was used.