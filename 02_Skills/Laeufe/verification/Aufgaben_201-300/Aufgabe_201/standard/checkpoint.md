# Checkpoint

Implemented unified rule `segment` YAML handling through `SegmentEmbed`, with string and keys/operator object formats. Added normalization of one-key objects to OR in import, filesystem snapshots, SQL rule and rollout persistence, and canonical object export. Updated requested fixtures and added focused tests.

Local tooling: `rg` was unavailable (`/bin/bash: line 1: rg: command not found`), so inspection used `grep` and `find`.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./internal/ext ./internal/storage/fs ./internal/storage/sql` exited 0; all three packages reported `ok`. `git diff --check` exited 0. The first test run had a snapshot return-signature compile error and an export fixture mismatch; both were corrected before the final run.
