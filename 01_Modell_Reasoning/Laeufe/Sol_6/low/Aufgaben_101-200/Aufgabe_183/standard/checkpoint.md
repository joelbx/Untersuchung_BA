Task: correct Ubuntu 20.04 and 22.04 lifecycle metadata.
Status: implemented and verified.
Tests: GOPROXY=off go test ./config (passed); GOPROXY=off go test ./gost -run ^TestUbuntu_Supported$ -count=1 (passed).
