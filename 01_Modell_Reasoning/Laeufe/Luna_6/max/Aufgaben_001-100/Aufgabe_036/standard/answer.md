Added database pool options to [config.go](/app/config/config.go) and mapped their config keys in `Load`. The loader now reads `meta.check_for_updates`; its default is `false`, so omitted keys retain that value and the default config fixtures still match `Default()`.

Updated the existing advanced config fixture and expectation to cover the pool options and an explicit update-check value.

**Verification:** `go test ./config` and `git diff --check` passed.