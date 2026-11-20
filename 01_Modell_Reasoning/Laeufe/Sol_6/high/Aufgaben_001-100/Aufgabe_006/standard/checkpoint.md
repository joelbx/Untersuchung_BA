Task: implement generic fanoutbuffer in /app.
Status: complete. Added lib/utils/fanoutbuffer/buffer.go and buffer_test.go. The buffer supports ordered independent cursors, fixed ring plus overflow, grace expiry, blocking notifications, close semantics, and reclamation.
Verification: GOPROXY=off GOTOOLCHAIN=local go test -race ./lib/utils/fanoutbuffer passed; GOPROXY=off GOTOOLCHAIN=local go test ./lib/services -run 'TestFanout' -count=1 passed; git diff --check passed.
Constraints observed: local code/tests only; no git history, index, or harness changes.
