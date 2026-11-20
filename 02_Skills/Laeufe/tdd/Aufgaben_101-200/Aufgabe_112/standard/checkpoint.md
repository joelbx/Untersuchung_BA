# Checkpoint

Task: integrate Fortinet CVE detection, enrichment, and reporting.
Status: inspecting repository; test-first implementation pending.

Offline test obstacle: `GOPROXY=off GOSUMDB=off go test -mod=mod ./models ./detector -run 'TestConvertFortinetToModelPreservesAdvisory|TestFortinetContentAppearsBeforeNvd|TestFortinetConfidenceUsesStrongestSource|TestDetectCveByCpeURIKeepsFortinetWithoutJVN' -count=1` stopped before compilation: `go: github.com/pelletier/go-toml/v2@v2.0.8: module lookup disabled by GOPROXY=off`. RED behavior could not be observed; implementation proceeds against locally inspected models and tests. No dependency download attempted.

Implementation complete: Fortinet-capable go-cve-dictionary version and cached compatible indirect versions; Fortinet CPE matching, confidence, advisory IDs, conversion, enrichment, report source links and display order. Added model, detector and HTTP fixture regression tests. Observed RED for source-link selection, multi-advisory storage, and end-to-end detection/enrichment; initial RED for new model tests was blocked by the unavailable cached transitive version noted above.

Verification: `GOPROXY=off GOSUMDB=off go test -mod=readonly ./...` passed across all packages after the final edit. `git diff --check` passed. The earlier offline dependency obstacle was resolved by selecting locally cached compatible indirect versions; no dependencies were downloaded.
