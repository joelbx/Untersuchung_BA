# Checkpoint

- Task: support digest based image references throughout configuration, scanning, and reporting.
- Initial state: working tree clean; repository has Go packages in config, models, scan, and report.
- Implemented: digest fields, exclusive tag/digest validation, full reference construction, scan model propagation, numeric image server names, digest aware logging and report UUID names, and original server config lookup for image results.
- Added focused tests for validation, names, conversion, image server indexing, JSON round trip, and report UUID identifiers.
- Verification: `GOPROXY=off GOSUMDB=off go test -vet=off ./config ./models ./scan ./report ./commands -skip '^TestScan$'` passed; `git diff --check` passed.
- Full default test run is limited by pre-existing `go vet` warnings in `models/library.go`; with vet disabled, `models.TestScan` fails because the local Trivy vulnerability database is not populated. No downloads were requested.
- Repository edits are complete.
