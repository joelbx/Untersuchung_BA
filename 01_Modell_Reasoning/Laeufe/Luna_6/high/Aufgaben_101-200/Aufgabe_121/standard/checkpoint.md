# Checkpoint

Task: add readable authentication method matching as a Rego built-in in the authz engine.

Implemented `flipt.is_auth_method` in `internal/server/authz/engine/ext`, registered it with OPA as a two-argument built-in, mapped the supported names to generated protobuf enum constants, and imported the extension from the Rego engine so it is registered at runtime. Added focused coverage for all supported mappings, mismatch behavior, missing authentication, and unsupported names.

Verification: `go test ./internal/server/authz/engine/ext ./internal/server/authz/engine/rego` passed.
