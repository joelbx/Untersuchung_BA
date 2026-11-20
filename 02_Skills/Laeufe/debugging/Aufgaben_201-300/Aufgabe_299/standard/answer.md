Added filesystem path completion to `:open`, including favorite paths, absolute paths, local `file:///` URLs, and `~` paths. The Filesystem category follows the configured category order, remains visible when empty, and is documented in the settings help.

Verification: 98 relevant tests passed, and `git diff --check` passed. `flake8` was unavailable in the local environment.