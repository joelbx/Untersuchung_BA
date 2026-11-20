# Checkpoint

Task: resolve WordPress vulnerability cache lookup indirection and inactive package filtering.

Implementation complete:
- Cache access now takes a direct `map[string]*string`; absent keys and nil cached pointers both return `("", false)`.
- WordPress integration passes the server's `config.WordPressConf` into scanning, and inactive filtering is controlled by that server's `IgnoreInactive` setting.
- Added the TOML tag for `ignoreInactive`, allowing the per-server setting to load from config files.
- Updated WordPress cache tests for direct map access and nil cached values; inactive filtering's active/inactive cases remain covered.

Validation:
- `GOPROXY=off go test ./wordpress ./config ./report` passed.
- `git diff --check` passed.
- Report package compilation emitted an existing SQLite C compiler warning about returning the address of a local variable; the package tests still passed.
