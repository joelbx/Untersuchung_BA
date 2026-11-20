Added filesystem path completion to `:open`. The Filesystem category follows `completion.open_categories`, shows `completion.favorite_paths` when the argument is empty, and suggests sorted local paths for absolute paths, `file:///` URLs, and `~` paths. Updated the settings help and completion tests.

Verification: 106 relevant tests passed; `git diff --check` passed.