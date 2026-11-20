# Checkpoint

Investigating list constraint operators. Initial repository search could not use `rg` because it is unavailable (`/bin/bash: rg: command not found`); using local `find` instead.

## Investigation
The operator maps omit both list operators, so create/update validation rejects them. `matchesNumber` parses every constraint value with `strconv.ParseFloat` before switching on the operator, so JSON arrays cannot evaluate. `matchesString` has no list branch and rejects an empty input before comparison. Both request validators share the same shape. Hypothesis: adding the operators to the maps, routing list operands through typed JSON unmarshalling, and validating list operands at both request entry points resolves the issue. A focused regression test was added and started before the fix.

## Resolution and verification
Added list operators to the public operator maps; evaluated string and numeric JSON lists with typed unmarshalling; validated list type and the 100-item limit in create/update requests. Date/time constraints remain excluded despite sharing the numeric operator map. A second regression test exposed malformed numeric lists being skipped when the context value was empty; list parsing now precedes that early return.

Executed `GOPROXY=off GOSUMDB=off go test ./rpc/flipt ./internal/server/evaluation -count=1`: both packages passed. Executed `git diff --check`: passed. Go test rewrote `go.work.sum`; restored its original checked-out content to keep the patch scoped.
