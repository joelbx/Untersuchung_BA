Added a configurable **Filesystem** category to `:open` completion. It shows `completion.favorite_paths` when the argument is empty and suggests matching local paths for absolute paths, `file:///` URLs, and `~` paths. The category follows the order in `completion.open_categories`; both settings are documented in the help.

Verification: 69 completion model tests and 31 config data tests passed.