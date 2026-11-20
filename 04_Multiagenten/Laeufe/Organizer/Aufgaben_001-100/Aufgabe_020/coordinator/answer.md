Added Redis TLS trust options for CA file paths, inline CA data, and optional certificate verification skipping. `NewClient` now builds the Redis connection with TLS 1.2 or newer, and config validation rejects both CA options together. I also added YAML fixtures, updated the schemas, and registered `api/cachetls` in the integration matrix.

The full short config and Redis cache test suites passed. Targeted command and integration harness build checks passed, as did `git diff --check`. The Dagger integration case compiled but was not run locally.

Delegation: none; I implemented the changes directly.