Task: support image digests throughout config validation, scanning, and reporting.
Status: implemented and verified.
Changes: added Digest to config and scan result images; added config.Image.GetFullName; enforced exactly one tag or digest with specified errors; propagated digest into scan results; used full reference for scanning, logging, and report identifiers; changed per-image server names to numeric index@original server.
Tests: GOPROXY=off GOSUMDB=off go test ./config ./scan ./report passed. Full affected-package run with -vet=off passed config/scan/report; models TestScan failed in existing library vulnerability fixture. Default full run also reports existing models/library.go vet warnings.
Delegation: none.
