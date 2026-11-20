# Checkpoint

Task: add explicit CVSS v4.0 storage to CveContent, capture NVD v4.0 metrics during conversion with their sources, and aggregate source scores in Mitre-then-Nvd order.

The CVSS v4.0 CveContent fields and MITRE conversion were already present. The original go-cve-dictionary pin lacked Nvd.Cvss40; the module was advanced to a compatible version already in the local cache, without fetching. ConvertNvdToModel now captures score, vector, and severity per metric source, and Cvss40Scores aggregates Mitre then Nvd. The existing aggregation test now covers both sources.

Verification: `GOPROXY=off GOSUMDB=off go test ./models` passed. `git diff --check` passed.
