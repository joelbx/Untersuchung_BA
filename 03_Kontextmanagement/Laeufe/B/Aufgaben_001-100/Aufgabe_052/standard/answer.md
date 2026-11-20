Implemented token counts for `Chat.Complete` and `Agent.PlanAndExecute`, including usage across agent steps and streaming responses. Updated callers to use the returned counts.

The focused chat and model tests pass, and `git diff --check` is clean. Broader package tests could not run because required native headers are unavailable. The repository work item is complete.