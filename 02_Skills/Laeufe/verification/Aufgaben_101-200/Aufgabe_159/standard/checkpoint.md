# Checkpoint

Issue: `parsePkgName` must split or normalize Maven, PyPI, Golang, npm, and Cocoapods names into namespace, name, and subpath.

Changes: Added `parsePkgName` in `reporter/sbom/cyclonedx.go`, mapped scanner and manifest aliases to canonical PURL types, and used parsed fields in library and GitHub dependency PURLs. Added direct parser and PURL construction tests in `reporter/sbom/cyclonedx_test.go`.

Verification: `GOPROXY=off GOSUMDB=off go test ./reporter/...` exited 0: reporter and reporter/sbom passed. `git diff --check` exited 0. Both commands were run after the final test edit.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used `grep` and `find` for repository search.
