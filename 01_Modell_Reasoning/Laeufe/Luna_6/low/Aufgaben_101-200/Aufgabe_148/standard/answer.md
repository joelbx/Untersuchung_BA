Implemented Teleport-Proxy SSH support in the multiplexer. Prefixed connections are classified as SSH, the metadata header is consumed, and a valid `ClientAddr` is exposed through `RemoteAddr()`. Standard SSH handling remains unchanged.

Added focused coverage for routing, header removal, and the remote address. `go test ./lib/multiplexer` and `git diff --check` pass.

The required checkpoint is at `.codex-role-output/checkpoint.md`.