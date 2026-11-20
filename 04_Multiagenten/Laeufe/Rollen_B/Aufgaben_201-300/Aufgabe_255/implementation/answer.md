Updated the password lookup plugin to parse term parameters through `LookupModule`, use plugin options as defaults, and accept `chars` as either a comma-separated string or a list. Inline values take precedence, and repeated `/dev/null` lookups with the same seed are deterministic.

Updated the unit tests. All 34 password lookup tests pass, and `git diff --check` is clean.