# Checkpoint

Issue resolved in checked-out files: U2F challenges now cover all registered devices, while the response keeps the legacy top-level challenge and adds `challenges`. Auth clients and CLI accept both legacy and multi-device responses. Web handlers forward the enhanced response. `tsh mfa` remains hidden.

Verification: `go test ./lib/auth ./lib/client ./lib/web ./tool/tsh -count=1` passed. Focused `go test ./lib/web -check.f TestU2FLoginWithMultipleDevices -count=1` passed. `git diff --check` passed.

Delegation: none.
