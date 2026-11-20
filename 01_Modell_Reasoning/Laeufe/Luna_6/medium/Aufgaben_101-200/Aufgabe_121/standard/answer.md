Implemented and registered `flipt.is_auth_method` in the Rego engine. It supports `token`, `oidc`, `kubernetes`/`k8s`, `github`, `jwt`, and `cloud`, matching their protobuf enum codes and existing `METHOD_*` string inputs. Missing authentication and unsupported method names return the specified errors.

Added tests covering supported methods, the `k8s` alias, mismatches, and error cases. Both focused packages pass:

`go test ./internal/server/authz/engine/rego ./internal/server/authz/engine/ext`