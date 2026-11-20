Added filesystem completion to `:open`. The new `Filesystem` category follows `completion.open_categories` order, suggests local paths, `file:///` URLs, and `~` paths, and shows `completion.favorite_paths` when the argument is empty. I updated the settings help and added tests.

Verification: 321 tests passed, 1 skipped, and 1 expected failure in the completion and config test suites.