Implemented the WordPress cache and inactive package fixes. Cache lookups now use the map directly and treat nil values as misses. The scanner reads `IgnoreInactive` from the server’s WordPress configuration.

`go test ./wordpress ./report` and `git diff --check` passed.