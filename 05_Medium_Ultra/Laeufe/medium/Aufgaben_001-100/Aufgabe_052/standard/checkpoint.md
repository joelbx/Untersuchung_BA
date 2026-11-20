Task: implement token accounting for Chat.Complete and Agent.PlanAndExecute, including streaming and multi-step aggregation.
Status: complete.
Changes: new TokenCount API and cl100k_base counters; agent counts prompts and streamed/completed responses across steps; chat/assist/web call sites updated; new counter and multi-step tests.
Verification: go test lib/ai/chat.go lib/ai/client.go lib/ai/chat_test.go passed; go test ./lib/ai/model passed; go test -race lib/ai/chat.go lib/ai/client.go lib/ai/chat_test.go passed; git diff --check passed.
Limitation: full ./lib/ai/... ./lib/assist test run blocked by missing system C headers; disabling cgo exposes optional hardware/PKCS#11 dependency build errors.
