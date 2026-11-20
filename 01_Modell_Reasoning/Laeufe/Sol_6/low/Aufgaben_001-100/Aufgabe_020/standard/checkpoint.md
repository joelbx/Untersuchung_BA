Task: Add Redis cache TLS trust configuration, validation, YAML coverage, and api/cachetls integration matrix entry.
Status: Implemented Redis NewClient with TLS 1.2, custom CA path/inline PEM, system fallback, insecure option, and exclusive-input validation. Wired into gRPC cache startup. Added schema, fixtures, config and client tests, and TLS Redis integration case/matrix entry.
Verification: Focused internal/config and internal/cache/redis tests pass. Command and integration package compilation still running. git diff --check passes.
