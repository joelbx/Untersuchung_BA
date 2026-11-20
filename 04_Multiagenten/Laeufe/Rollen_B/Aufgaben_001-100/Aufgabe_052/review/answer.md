VERDICT: FIX

**Code defect:** [agent.go](/app/lib/ai/model/agent.go:374) returns a streaming response before all tokens arrive. If the caller then calls `CountAll()`, [tokencount.go](/app/lib/ai/model/tokencount.go:148) finalizes the counter, and later streamed text is ignored. The returned count can permanently underreport completion usage. Finalize the count only after the stream has finished.

**TEST_ENVIRONMENT_PROBLEM:** `GOPROXY=off GOSUMDB=off go test ./lib/assist ./lib/web -run 'TestChatComplete|Test_runAssistant' -count=1` exited 1 during compilation: Linux headers were missing, and SQLite C symbols were unavailable. Supply the required native headers and compatible toolchain, then rerun.

`GOPROXY=off GOSUMDB=off go test ./lib/ai/model ./lib/ai` exited 0; both packages passed. No project code was changed.