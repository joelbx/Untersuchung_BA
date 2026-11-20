# Checkpoint

Issue resolved: Chat.Complete and Agent.PlanAndExecute return TokenCount; per-step prompt/completion usage and streaming usage are accounted for through the new model API. Assist and web consumers updated.
Verification: `go test ./lib/ai/model ./lib/ai` passed; `git diff --check` passed. `go test ./lib/assist` could not build due missing native C headers and sqlite C compilation errors in dependencies. An optional race run was stopped while compiling dependencies.
No delegation used. Git history, index baseline, and harness configuration untouched.
