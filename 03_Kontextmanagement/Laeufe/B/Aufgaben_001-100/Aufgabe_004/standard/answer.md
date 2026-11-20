Resolved the PassAliases drawer issue. It now shows the full aliases list or an explicit “No aliases” state, and “Get an alias” opens the creation modal. The provider creates a vault when needed and refreshes cached aliases after creation.

Validation passed: 6 existing tests, Components and Pass type checks, targeted lint, and `git diff --check`.