Task: Add -wp-ignore-inactive configuration and skip inactive WordPress plugin/theme lookups.
Status: Implemented and verified. Flag available in report, server, and tui. TOML config loads wpIgnoreInactive; FillWordPress filters inactive packages before API requests. Focused tests added.
Verification: GOPROXY=off GOSUMDB=off go test -p 1 ./config ./wordpress ./commands ./report passed; git diff --check passed.
Constraints: Local code/tests only; git history and index baseline unchanged.
