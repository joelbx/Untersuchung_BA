Updated [oval/util.go](/app/oval/util.go) so `major("")` returns `""` without panicking. Added an empty-input case to the existing test; non-empty parsing is unchanged.

`GOPROXY=off GOSUMDB=off go test ./oval` passed. No delegation was used.