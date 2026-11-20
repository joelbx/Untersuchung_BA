# Checkpoint

Task: correct `parsePkgName` namespace, name, and subpath parsing for Maven, PyPI, Golang, npm, and Cocoapods.

Complete: added `parsePkgName` with three string results; integrated it into library and dependency graph PURL construction. Manifest ecosystem aliases are supported. Added table tests for requested cases and representative aliases. `GOPROXY=off GOSUMDB=off go test ./reporter/sbom ./reporter` passed. `git diff --check` passed. No git history, index baseline, or harness configuration changes.
