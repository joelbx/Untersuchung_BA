VERDICT: FIX
Code defect: Amazon 2023 point/build releases such as 2023.0.20230322 pass through scanner/redhatbase.go:280-284 but config/os.go:337-349 returns unknown. GetEOL then returns found=false; oval/util.go:333-338 selects unknown instead of 2023. Normalize supported year-based releases with their dotted build suffix before EOL and OVAL lookup.
Tests: GOPROXY=off GOSUMDB=off go test ./config ./oval ./scanner — PASS (all three packages).
No TEST_ENVIRONMENT_PROBLEM. No project code or tests changed.
