# Checkpoint

- Task: add digest-aware image configuration, scanning, and reporting.
- Status: implementation and targeted verification complete.
- Changed: digest fields, full image references, validation, scan conversion, OS detection naming, and report UUID naming.
- Verification: config, scan, report, and scan result model tests pass with `-vet=off` and downloads disabled.
- Existing test limits: model package vet fails in `models/library.go`; its `TestScan` needs a local Trivy vulnerability database.
