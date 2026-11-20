Task: add per-server external nmap port scanning with configuration and validation.
Status: complete. Added technique mapping and validation, per-server TOML loading, native/external dispatch, nmap XML parsing, discovery example, and focused tests.
Verification: GOPROXY=off go test ./config ./scanner ./subcmds passed; git diff --check passed.
Constraints: local repository only; git history/index and harness settings untouched.
