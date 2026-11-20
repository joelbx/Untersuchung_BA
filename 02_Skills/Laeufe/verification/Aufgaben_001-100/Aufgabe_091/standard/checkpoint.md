# Checkpoint

Task: add `isoneof` and `isnotoneof` string and number constraint support.

Initial state: working tree clean. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use `find` and `grep`.

Implementation: added both list operators to the public constants and applicable maps; evaluator now parses typed JSON arrays and checks membership; constraint create/update validation rejects invalid lists and lists over 100 items. Added focused evaluator and request validation tests, including empty strings and malformed numeric lists with empty context values.

Verification:
- `GOPROXY=off go test -count=1 ./rpc/flipt ./internal/server/evaluation` exited 0: both packages passed.
- `git diff --check` exited 0.
- The Go test command changed `go.work.sum` automatically; restored that unrelated change from `HEAD` after testing.
