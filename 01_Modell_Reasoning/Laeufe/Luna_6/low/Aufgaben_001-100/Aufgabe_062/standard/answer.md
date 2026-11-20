Implemented terminal restoration for abandoned password reads and `Close`, added `NotifyExit`, and made password reads that expire by deadline return an empty result with `context.DeadlineExceeded`.

Verification: `go test ./lib/utils/prompt` passed; `git diff --check` passed.