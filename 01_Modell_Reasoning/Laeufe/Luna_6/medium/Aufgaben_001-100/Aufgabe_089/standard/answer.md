I started the validation API change and wrote [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md), but the fix is incomplete. The existing CLI and tests still use the old `(Result, error)` API, and I haven’t implemented the exported snapshot constructors or verified the repository tests.

I can’t claim the issue is resolved in this state.