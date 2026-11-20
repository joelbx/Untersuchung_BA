Resolved the PassAliases drawer issue. Vault lookup no longer creates a vault during initialization; opening the creation flow creates one when needed. The provider now loads and caches aliases, and the empty drawer shows “No aliases.”

The existing PassAliases tests pass (3/3). Type checks pass for `@proton/components` and `@proton/pass`.