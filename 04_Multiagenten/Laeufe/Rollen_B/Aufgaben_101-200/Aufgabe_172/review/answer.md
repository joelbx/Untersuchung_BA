VERDICT: FIX

The patch parses legacy string entries, but [AffectedProcess.ListenPorts](/app/models/packages.go:181) now rejects object entries written by the previous schema. [Report loading](/app/report/util.go:750) will fail on those saved results. Add a compatibility decoder that accepts both forms and preserves reachability data.

`GOPROXY=off GOSUMDB=off go test ./models ./scan ./report` passed for all three packages. There was no test environment problem. Review only; no project code or tests were changed.