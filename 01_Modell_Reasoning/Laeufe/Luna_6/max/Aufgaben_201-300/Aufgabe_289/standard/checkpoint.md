# Checkpoint

Task: resolve the configuration defaults and decode hook issue in `/app`.

Completed:
- Exported `DecodeHooks`; `Load` composes a copy of that hook slice with the experimental field skip hook.
- Added `DefaultConfig()` using the existing test fixture values and made the fixture delegate to it.
- Added the `version` mapstructure tag.
- Changed storage `Local` and `Git` fields to pointers and made validation handle missing sub-configurations safely.
- Updated existing storage test fixtures for the pointer fields.

Verification:
- `go test ./internal/config` passed.
- `go test ./internal/cmd` passed.
- `git diff --check` passed.
