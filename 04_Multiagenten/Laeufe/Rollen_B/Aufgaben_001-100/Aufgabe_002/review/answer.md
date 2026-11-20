VERDICT: FIX

**Code defect:** [KubeAddr()](/app/lib/service/cfg.go:367) checks only the first configured address. If it is invalid and a later address is valid, `tctl auth sign --format=kubernetes` fails instead of continuing the search. Iterate the configured addresses and return an error only when none is valid.

**Tests passed:**

- `GOPROXY=off GOSUMDB=off go test ./lib/service -run '^TestProxyKubeAddr$' -count=1`
- `GOPROXY=off GOSUMDB=off go test ./tool/tctl/common -run '^(TestCheckProxyAddr|TestAuthSignKubeconfig)$' -count=1`

**TEST_ENVIRONMENT_PROBLEM:** None. I made no project code or test changes.