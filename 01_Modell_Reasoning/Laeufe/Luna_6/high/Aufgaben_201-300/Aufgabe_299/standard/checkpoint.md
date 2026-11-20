# Checkpoint

Task: implement filesystem path completion in `:open`, including category configuration, favorite paths, path/file URL matching, and help documentation.

Implemented `FilePathCategory`, integrated it according to `completion.open_categories`, added `completion.favorite_paths`, and updated settings help. The category handles empty-pattern favorites, absolute paths, `file:///` paths, and `~` paths; suggestions are sorted and directories include a trailing separator.

Verification: Python compilation and `git diff --check` passed. Of the existing completion model tests, 65 passed when excluding the two tests whose exact old category expectations conflict with the newly required default Filesystem category. Running the whole file gives those same 2 failures (`test_url_completion_no_quickmarks` and `test_url_completion_no_bookmarks`) because both use the updated default config but expect only the previous categories.
