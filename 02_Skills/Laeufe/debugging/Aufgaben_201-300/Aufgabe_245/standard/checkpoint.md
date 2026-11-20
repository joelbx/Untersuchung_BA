# Checkpoint

Task: Refactor detectScanDest to group deterministic, deduplicated port slices by IP and update consumers.

Status: Investigating root cause and call sites. `rg` is unavailable in the environment; using local grep/find fallback.

Investigation: `detectScanDest` in scan/base.go already builds `map[string][]string`, then flattens it into a `[]string` and deduplicates full `ip:port` strings. Map iteration makes the returned slice order unstable. `scanPorts` passes this slice to `execPortsScan`, which dials each combined address and returns open `ip:port` strings for `updatePortStatus`. Existing tests in scan/base_test.go check the flat shape. Working pattern: `findPortScanSuccessOn` and `updatePortStatus` consume open `ip:port` strings, so only the input side of `execPortsScan` needs conversion. Hypothesis: retain the address-to-ports map, expand wildcard addresses into it, deduplicate/sort each port slice, and iterate sorted addresses in `execPortsScan`; this preserves the downstream open-port representation.

Verification: Before the fix, `GOPROXY=off GOSUMDB=off go test ./scan -run '^Test_detectScanDestGroupsAndSortsPorts$' -count=1` failed as expected: returned `[127.0.0.1:80 127.0.0.1:22 192.168.1.1:22]` instead of the grouped map. After the fix, `GOPROXY=off GOSUMDB=off go test ./scan -run '^Test_detectScanDest' -count=1` passed, and `GOPROXY=off GOSUMDB=off go test ./scan -count=1` passed. `git diff --check` passed. The Go compiler emitted an existing warning from the cached sqlite3 C dependency; tests still passed.

Result: `detectScanDest` returns a non-nil map, expands wildcard listeners into configured IPv4 addresses, sorts and deduplicates ports per address. `execPortsScan` accepts that map and scans sorted addresses while keeping its existing open-port output for `updatePortStatus`.
