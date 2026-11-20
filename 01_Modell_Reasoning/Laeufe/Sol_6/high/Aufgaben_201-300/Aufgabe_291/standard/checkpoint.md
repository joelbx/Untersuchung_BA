# Checkpoint

Task: expose NVD CVSS v4.0 metrics alongside MITRE.
Status: complete. NVD conversion maps each CVSS 4.0 metric by source; score aggregation includes Mitre then Nvd. Existing CveContent fields already store CVSS 4.0. Updated go-cve-dictionary to the locally cached version that defines Nvd.Cvss40 and added regression tests.
Verification: focused model tests and full models suite passed with GOPROXY=off, GOSUMDB=off, GOTOOLCHAIN=local. git diff --check passed. Wider detector/reporter run was stopped during dependency compilation; no test failure was observed.
Constraints: local code and tests only; git history and index unchanged.
