`detectScanDest` now returns a non-nil `map[string][]string` with ports grouped by IP, deduplicated, and sorted. I updated `execPortsScan` to consume the map and changed the existing tests to expect the new format.

The new regression test failed against the old behavior and passes with the fix. The full `scan` package tests and `git diff --check` also pass.