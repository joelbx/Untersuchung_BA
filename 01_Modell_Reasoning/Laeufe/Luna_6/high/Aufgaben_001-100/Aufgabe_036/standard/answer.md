Implemented the config loader updates in [config.go](/app/config/config.go):

- Added `MaxIdleConn`, `MaxOpenConn`, and `ConnMaxLifetime`, with mappings from the requested `db.*` keys.
- Mapped `meta.check_for_updates` and set its default to `false`.
- Gave each `Load` call a fresh Viper instance so values from earlier loads cannot carry over.

Updated the advanced config fixture and expected values. `go test ./config` and `git diff --check` passed.