VERDICT: ACCEPT

The patch matches the requested EOL dates and Windows KB additions. The new rollups preserve earlier entries, follow revision order, and use named struct literals. I found no blocking defect. The patch also updates FreeBSD 13/14 dates outside the requested scope.

Relevant local tests passed:

- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./config -run 'TestEOL_IsStandardSupportEnded' -count=1`
- `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./scanner -run 'Test_windows_(detectKBsFromKernelVersion|recentRollupsFromKernelVersion)$' -count=1`
- `git diff --check`