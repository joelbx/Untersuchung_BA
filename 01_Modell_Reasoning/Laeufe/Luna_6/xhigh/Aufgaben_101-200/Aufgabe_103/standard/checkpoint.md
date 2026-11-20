# Checkpoint

Task: fix RPM package output parsing and source RPM filename validation in `/app`.

Completed:
- Preserved empty RPM queryformat fields in normal and repoquery package parsing, including Amazon Linux 2 format selection.
- Constructed package EVR strings consistently for epochs `0`, `(none)`, empty epochs, and nonzero epochs, omitting an empty release suffix.
- Added `-src.rpm` source filename support and stricter malformed filename checks.
- Fixed update candidate parsing for CentOS and Amazon Linux layouts, including epoch and empty release handling.
- Added regression tests for these cases.

Validation: `gofmt` completed, `go test ./scanner` passed, and `git diff --check` passed.
