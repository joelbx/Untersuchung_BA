Added filesystem completion to `:open`. The new `Filesystem` category follows `completion.open_categories` order, shows `completion.favorite_paths` when the argument is empty, and suggests sorted local paths for absolute paths, `file:///` URLs, and `~` paths. I updated the configuration help and tests.

Verification: 100 completion and config tests passed. No delegation was used.