# Checkpoint

Task: fix terminal restoration and cancellation behavior in `lib/utils/prompt` ContextReader and expose `NotifyExit`.

Initial inspection: relevant implementation and tests are in `lib/utils/prompt/context_reader.go`, `stdin.go`, and `context_reader_test.go`. Next: inspect these files and repository guidance, implement focused changes, and run existing package tests.
