Implemented the PassAliases provider hook, alias fetching helpers, and explicit vault lookup/creation behavior. The drawer now shows a clear “No aliases” state, and the creation flow can create a vault when needed.

Verification passed: the targeted PassAliases suite (3 tests), the components type check, and `git diff --check`.