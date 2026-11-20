Fixed public bookmark session restoration. `getLastPersistedLocalID` now returns `null` when no valid ID exists, ignores invalid keys, preserves a valid ID of `0`, and leaves storage untouched. The bookmark hook resumes a session only when an ID is found, then continues to list bookmarks.

The two relevant Jest suites passed: **19 tests**. `git diff --check` also passed.