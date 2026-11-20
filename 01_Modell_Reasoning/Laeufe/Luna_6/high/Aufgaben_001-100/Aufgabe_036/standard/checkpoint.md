# Checkpoint

Task: Fix config loading for database pool settings and `meta.check_for_updates`, preserving defaults for omitted keys and matching `Default()` when loading the shipped default/deprecated configs.

Completed: Added database pool fields and key mappings, mapped `meta.check_for_updates`, set the omitted update-check default to false, and isolated Viper state per `Load` call to prevent values leaking between files. Updated the advanced fixture to cover explicit pool settings and the update flag.

Verification: `go test ./config` passed; `git diff --check` passed.
