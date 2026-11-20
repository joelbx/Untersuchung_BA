Updated the WordPress cache lookup to accept the map directly and report key presence with comma-ok lookup. The scan now receives the server’s `WordPressConf` and uses its `IgnoreInactive` setting to filter plugins and themes by `Status`.

Verified with `go test ./wordpress ./report`; both packages passed. `git diff --check` also passed.

The cache uses `map[string]string`, so individual nil values cannot occur. Nil maps return `("", false)`; empty-string entries remain cache hits.