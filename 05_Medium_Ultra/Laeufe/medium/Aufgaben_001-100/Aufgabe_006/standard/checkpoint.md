Task: Implement the generic fanoutbuffer package in /app.
Status: Complete. Added lib/utils/fanoutbuffer/buffer.go and focused tests. The package race tests and existing lib/services fanout tests pass.
Verification: GOPROXY=off GOTOOLCHAIN=local go test -race ./lib/utils/fanoutbuffer; GOPROXY=off GOTOOLCHAIN=local go test ./lib/services -run Fanout -count=1.
