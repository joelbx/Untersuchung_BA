Updated [config.go](/app/internal/config/config.go) so scalar strings decoded into `[]string` split on spaces, tabs, and newlines. Empty strings produce an empty slice, and existing sequences pass through unchanged. Empty environment values now follow the same behavior as YAML.

Updated the CORS fixture and added tests for YAML and environment inputs. `go test ./internal/config` passes.