# Checkpoint

Task: Add canonical OS EOL data and evaluation, emit EOL warnings in scan summaries, and centralize major version parsing.

Status: Implemented. The EOL mapping and warning evaluation are in `config/os.go`; scan results use the scan timestamp and summaries print each warning as `Warning: <message>`. OS family constants now live with the EOL model. Major version parsing is shared through `version.Major` and exposed as `util.Major`.

Verification: `go test ./...` passed. After the final warning rendering adjustment, `go test ./report` passed. `git diff --check` passed.
