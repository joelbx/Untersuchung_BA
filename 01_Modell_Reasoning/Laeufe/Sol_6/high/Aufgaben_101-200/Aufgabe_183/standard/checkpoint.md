# Checkpoint

Task: Correct Ubuntu 20.04 extended support lifecycle and add Ubuntu 22.04 lifecycle metadata.

Status: Complete. Added Ubuntu 20.04 extended support through April 1, 2030 and Ubuntu 22.04 standard/extended support through April 1, 2027/2032. Enabled Ubuntu 22.04 in Gost and OVAL CVE lookup paths, with lifecycle and Gost test coverage.

Validation: `GOPROXY=off GOSUMDB=off go test ./config ./gost ./oval` passed; `gofmt -l` and `git diff --check` clean.
