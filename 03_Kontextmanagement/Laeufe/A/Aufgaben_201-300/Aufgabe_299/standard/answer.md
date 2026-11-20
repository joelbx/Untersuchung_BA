Added filesystem path completion to `:open`. The Filesystem category shows configured favorite paths for an empty input and suggests local files and directories for absolute paths, `file:///` URLs, and `~` paths. Category order is configurable, and the settings help is updated.

Verification: 97 completion and config tests passed; `git diff --check` passed.