VERDICT: ACCEPT
Reviewed the applied diff in config/os.go, config/os_test.go, gost/ubuntu.go, and gost/ubuntu_test.go. Ubuntu 20.04 extended support ends 2030-04-01; Ubuntu 22.04 standard/extended support ends 2027-04-01/2032-04-01. Gost accepts release 2204 for CVE processing. No code defect found. `git diff --check` passed.
Tests executed successfully:
- `GOPROXY=off GOSUMDB=off go test ./config ./gost -run 'TestEOL_IsStandardSupportEnded|TestGetEOLUbuntuLTSDate|TestUbuntu_Supported' -count=1`
- `GOPROXY=off GOSUMDB=off go test ./config ./gost -count=1`
- `GOPROXY=off GOSUMDB=off go test ./models -count=1`
