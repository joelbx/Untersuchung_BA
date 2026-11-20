Updated Proton Drive’s persisted session lookup to return `number | null`, accept only numeric `ps-` keys, preserve the valid ID `0`, and leave localStorage untouched. The public bookmark hook now resumes a session only when an ID exists, restoring its saved key password before listing bookmarks.

The two relevant Jest suites passed: 17 tests total. `git diff --check` also passed.