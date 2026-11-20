Resolved the PassAliases drawer issue. It now shows the full aliases list or a clear “No aliases” state, and the creation button opens the modal. Vault lookup no longer creates a vault; the creation flow does that when needed and refreshes the alias list after saving.

Verification passed: all 9 PassAliases tests, components and Pass type checks, Prettier, and `git diff --check`.