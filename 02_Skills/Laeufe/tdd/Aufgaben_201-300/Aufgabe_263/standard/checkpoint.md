# Checkpoint

Task: migrate DynamoDB audit event metadata from legacy `Fields` JSON strings to native `FieldsMap` maps.

Implementation: new writes use `FieldsMap`; both formats remain readable. Background migration runs after the existing RFD 24 migration, with distributed locking, consistent paginated scans, batch writes, retries, idempotent filtering, semantic validation, and progress/error logging. Added `backend.FlagKey` under `/.flags`.

TDD: watched tests fail for string storage, missing migration helper, malformed trailing JSON, empty-string loss, and missing `FlagKey`; focused tests now pass.

Checks: `go test ./lib/events/dynamoevents ./lib/backend -count=1` passed. The AWS integration suite requires `TEST_AWS`, so it was skipped; live DynamoDB migration remains unverified here. `timeout 180s go test ./... > /tmp/teleport-go-test.log 2>&1` exited 124 (timeout); output reached four packages and reported no test failures before the timeout. Full suite outcome remains unknown. `git diff --check` passed.

Environment: `rg` unavailable (`/bin/bash: rg: command not found`), used grep/find. No external research or downloads.
