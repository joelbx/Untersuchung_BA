# Checkpoint

Task: Add NVD CVSS v4.0 storage, conversion, and aggregation alongside MITRE.
Status: Complete.
Changes: Updated the locally cached go-cve-dictionary version to one with Nvd.Cvss40; mapped NVD CVSS 4.0 metrics by source into CveContent; included NVD after MITRE in Cvss40Scores; added focused conversion and aggregation tests. Existing CveContent v4.0 fields already satisfied the model requirement.
Validation: Offline focused tests and full models package tests passed; git diff --check passed.
Constraints observed: No external research, downloads, git history/index changes, or harness configuration changes.
