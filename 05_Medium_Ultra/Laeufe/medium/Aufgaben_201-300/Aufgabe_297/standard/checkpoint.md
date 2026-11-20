Task: implement trusted reverse proxy login with CIDR whitelist, frontend session initialization, and nested log redaction.
Status: complete.
Changes: ReverseProxyWhitelist, ReverseProxyUserHeader (default Remote-User), ReverseProxyDefaultUser; per-request UI proxy auth with user creation, first-user admin, last login update, JWT and Subsonic credentials; frontend session storage; recursive map and JSON redaction.
Verified: go test ./server/app ./log ./conf ./persistence ./server/subsonic; UI Jest 11 suites/35 tests; npm run check-formatting; git diff --check.
Constraints: local code/tests only; git history/index/harness unchanged.
