# Progress checkpoint

- Added the canonical EOL table and strict phase evaluators in `config/os.go`.
- Added lifecycle warning evaluation to per-target scan results and rendered warnings in scan summary order with `Warning: ` prefixes.
- Centralized major parsing behind `util.Major`, with shared internal parsing for `config.Distro.MajorVersion` to avoid an import cycle; updated Gost and OVAL callers.
- Added tests for exact mappings, missing releases, phase boundaries, warning wording, scan result integration, summary order, and major parsing.
- `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep` for repository searches.
- Verification: `GOPROXY=off GOSUMDB=off go test ./config ./util ./scan ./report ./oval ./gost && git diff --check` exited 0. All six packages passed. The SQLite C dependency emitted a compiler warning but no test failure.
