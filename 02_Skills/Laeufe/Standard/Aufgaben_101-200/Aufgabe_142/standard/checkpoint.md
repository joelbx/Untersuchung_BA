# Checkpoint

Working on expression AST, interpolation, matcher, and caller validation. `rg` is unavailable; using local `find` and `grep`.

Validation: `go test ./lib/utils/parse` passed. `go test ./lib/services ./lib/srv` encountered a local build blocker: `github.com/flynn/hid` failed with `/go/pkg/mod/github.com/flynn/hid@v0.0.0-20190502022136-f1b9b6cc019a/hid_linux.go:3:11: fatal error: linux/hidraw.h: No such file or directory`. Service/server behavior remains unverified by that command; trying CGO disabled.

`go test ./lib/services ./lib/srv` also reported local C compilation errors in `github.com/mattn/go-sqlite3`: `pread64` and `pwrite64` undeclared and `off64_t` unknown. `CGO_ENABLED=0 go test ./lib/services ./lib/srv` fails to compile local dependencies (`lib/bpf/bpf_nop.go: undefined Config`, `github.com/flynn/u2f/u2fhid: undefined hid.Devices`, `github.com/ThalesIgnite/crypto11: undefined pkcs11.ObjectHandle`). These checks have not passed; service and server tests remain unverified in this environment.

Final local verification: `go test ./lib/utils/parse` passed after the quoted-brace test was added. `git diff --check` passed. The two service/server test commands were stopped after their dependency build errors appeared; no service/server test results are claimed. CGO-disabled build additionally reported `lib/shell/shell.go:33:18: undefined: getLoginShell`.
