# Device enrollment limit investigation

Status: fix implemented and relevant enrollment tests passed.

Evidence: `GOPROXY=off GOSUMDB=off go test ./lib/devicetrust/enroll -run '^TestCeremony_RunAdminDeviceLimit$' -count=1` failed because `RunAdmin` returned a nil device after the fake service denied enrollment. Registration had already succeeded. The failure path returned `enrolled` from `Run`, which is nil on error, while the command prints a nonzero outcome by dereferencing that device. The initial test compilation also confirmed that `E.Service` was absent.

Pattern: the token creation error path in `RunAdmin` already returns `currentDev` with the partial outcome; the enrollment error path should do the same. The CLI printer needs a fallback when an outcome has no device information.

Verification: `GOPROXY=off GOSUMDB=off go test ./lib/devicetrust/enroll ./lib/devicetrust/testenv -count=1` passed after the final test change. `git diff --check` passed. A focused `tool/tsh/common` test build encountered missing local C headers (`linux/hidraw.h` and `gnu/libc-version.h`); the command was `GOPROXY=off GOSUMDB=off go test ./tool/tsh/common -run '^TestPrintEnrollOutcomeWithoutDevice$' -count=1`. It was stopped after the compiler errors, so its final exit code was 130. The fallback `CGO_ENABLED=0 GOPROXY=off GOSUMDB=off go test ./tool/tsh/common -run '^TestPrintEnrollOutcomeWithoutDevice$' -count=1` exited 1 because build constraints exclude all Go files in `lib/system`. CLI test execution remains unverified in this environment.

Plan: trace registration and enrollment error paths, reproduce with a focused test, make the smallest fix, then run relevant existing tests.
