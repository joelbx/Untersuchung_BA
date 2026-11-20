Implemented Redis cache TLS configuration in [NewClient](/app/internal/cache/redis/client.go). It supports a CA file, inline CA data, and `insecure_skip_tls`; TLS connections require at least TLS 1.2. Config loading rejects simultaneous CA path and inline data with the specified error.

Updated the config schemas and YAML fixtures, wired the constructor into Flipt, and added `api/cachetls` to the GitHub Actions integration matrix.

The targeted config, Redis, command, and schema tests pass. The integration harness compiles; the Dagger integration suite was not run locally.