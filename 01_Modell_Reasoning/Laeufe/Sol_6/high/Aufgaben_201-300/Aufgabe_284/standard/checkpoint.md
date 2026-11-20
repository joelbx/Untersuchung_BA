# Checkpoint

- Task: Replace the reverse tunnel server's local site slice with one instance and reuse its existing access point/cache.
- Status: Complete. The server owns one local site, uses its existing proxy access point, validates service certificate cluster names, and retains the local site through tunnel-close handling.
- Verification: `GOPROXY=off GOSUMDB=off go test ./lib/reversetunnel -count=1` passed; `git diff --check` passed.
- Constraints: Work only in the checked-out repository, preserve git history/index and harness configuration, run relevant existing tests.
