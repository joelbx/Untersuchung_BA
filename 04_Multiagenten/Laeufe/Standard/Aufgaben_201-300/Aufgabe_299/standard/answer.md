Added filesystem path completion to `:open`. The new **Filesystem** category follows the configured category order, shows `completion.favorite_paths` when the argument is empty, and suggests matching paths for absolute paths, local `file:///` URLs, and `~` paths. I updated the config and user help.

Verification: 68 completion tests and 31 config data tests passed; `git diff --check` passed.