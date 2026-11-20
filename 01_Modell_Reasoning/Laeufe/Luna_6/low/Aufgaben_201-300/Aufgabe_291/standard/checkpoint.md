# Checkpoint

Task: add NVD CVSS v4.0 persistence and include MITRE/NVD values in score aggregation.

Completed: NVD conversion copies score, vector, and severity from each v4.0 metric into the source keyed content; CVSS v4.0 aggregation visits sources in the required [Mitre, Nvd] order. Updated the pinned go-cve-dictionary revision because the previous revision has no NVD CVSS v4.0 field. The CveContent struct already had the required fields.

Verification: `go test ./models` passed; `git diff --check` passed.
