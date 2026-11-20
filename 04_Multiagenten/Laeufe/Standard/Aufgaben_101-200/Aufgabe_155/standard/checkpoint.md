Task: Add digest support to image configuration, scanning, and reporting.
Status: Implemented digest validation, full image references through scanning and reporting, model propagation, and local report directory creation for registry-qualified names. Added focused tests.
Verification: `go test -vet=off ./config ./scan ./report` passes; focused models image report test passes. Full models suite has an existing `TestScan` failure in `models/library_test.go`; default vet also fails on existing integer-to-string conversions in `models/library.go`.
