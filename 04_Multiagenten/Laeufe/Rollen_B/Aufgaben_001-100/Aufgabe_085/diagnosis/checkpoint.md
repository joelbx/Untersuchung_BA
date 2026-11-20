# Fault localization progress

Inspected the existing diff and report paths. `report/util.go:523` compares per-server scan results, then rebuilds Packages only from current.Packages. `getDiffCves` at line 552 iterates only current CVEs; it includes new CVEs and CVEs with updated metadata, but never previous-only CVEs. No DiffStatus type/field, CveIDDiffFormat, or CountDiff exists in models/vulninfos.go. The only existing diff test in report/util_test.go covers unchanged and plus-only data, with no status assertion. Config currently has one Diff bool and no plus/minus selection.

Diagnosis: implement plus/minus selection in report diff logic and its callers, classify by CVE map membership, carry status on VulnInfo, and rebuild package map from the scan matching each status. Formatting sites in report/util.go currently print raw CveID. Source/tests untouched per role constraint.
