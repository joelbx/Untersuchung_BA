Added filesystem completion to `:open`. The new `Filesystem` category shows `completion.favorite_paths` when the argument is empty and suggests sorted matches for absolute paths, local `file:///` URLs, and `~` paths. The config defaults and settings help now include the category and option.

Verification: 68 completion model tests and 31 config tests passed; `git diff --check` is clean.