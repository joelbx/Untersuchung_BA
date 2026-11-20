# Checkpoint
Task: remove database initialization for JWT-only authentication with non-database flag storage.
Implemented: per-method RequiresDatabase; conditional authentication DB initialization; cleanup gates; updated cleanup expectation; added config coverage.
Verification: go test ./internal/config ./internal/cleanup ./internal/cmd passed; git diff --check passed.
