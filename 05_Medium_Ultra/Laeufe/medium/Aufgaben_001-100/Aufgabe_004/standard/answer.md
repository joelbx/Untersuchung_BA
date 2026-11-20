Fixed the PassAliases drawer. It now shows existing aliases or a clear “No aliases” state, and “Get an alias” opens the creation modal. Vault lookup no longer creates a vault during drawer loading; the alias flow creates one when needed and refreshes the cached list after creation.

Verification passed: 3 focused drawer tests, TypeScript checks for Components and Pass, and `git diff --check`.