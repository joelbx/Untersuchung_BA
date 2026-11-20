VERDICT: FIX

**Code defect:** The scanner preserves a release such as `2023.0.20230322`, but [getAmazonLinuxVersion](/app/config/os.go:337) recognizes only the exact token `2023`. As a result, `GetEOL` returns `found=false` and the [OVAL lookup](/app/oval/util.go:333) uses `unknown`, leaving the reported Amazon Linux 2023 case unresolved. Normalize dotted build releases to their supported year before both lookups.

**Tests:** `GOPROXY=off GOSUMDB=off go test ./config ./oval ./scanner` passed for all three packages. No test environment problem.