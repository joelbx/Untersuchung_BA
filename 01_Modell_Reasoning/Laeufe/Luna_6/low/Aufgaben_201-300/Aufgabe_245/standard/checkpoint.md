# Checkpoint

Task: Refactor `scan.base.detectScanDest` to return IP-to-port slices, deduplicate and deterministically order ports, update consumers, and run relevant existing tests.

Initial discovery: implementation is in `scan/base.go`; direct tests and fixtures are in `scan/base_test.go`.
