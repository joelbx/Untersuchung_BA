Implemented Redis TLS trust configuration with custom CA paths, inline CA data, and optional certificate verification skipping. Redis connections now use TLS 1.2 or newer when `require_tls` is enabled, and conflicting CA options return the required validation error.

Added the `api/cachetls` integration case and workflow matrix entry, along with config fixtures and schema fields.

Checks passed: config tests, Redis tests in short mode, integration harness compilation, command package tests, and `git diff --check`. The full Redis tests use Testcontainers and were not run.

Key changes: [client.go](/app/internal/cache/redis/client.go), [cache.go](/app/internal/config/cache.go), [integration.go](/app/build/testing/integration.go), [integration-test.yml](/app/.github/workflows/integration-test.yml).