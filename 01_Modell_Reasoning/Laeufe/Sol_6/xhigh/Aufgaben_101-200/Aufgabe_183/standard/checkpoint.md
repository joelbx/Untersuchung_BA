# Checkpoint

Task: update Ubuntu lifecycle metadata so Ubuntu 20.04 extended support ends 1 April 2030 and Ubuntu 22.04 has standard support through 1 April 2027 and extended support through 1 April 2032.

Status: complete. Lifecycle dates added in `config/os.go`; Ubuntu 22.04 enabled in GOST and OVAL CVE paths; lifecycle and GOST tests extended. `go test ./config ./gost ./oval` and `go test ./scanner ./models` passed with local toolchain and network disabled. Diff review and `git diff --check` passed. Repository was clean at start.
