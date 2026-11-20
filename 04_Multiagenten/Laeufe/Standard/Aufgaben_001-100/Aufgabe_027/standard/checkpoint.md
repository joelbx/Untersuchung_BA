Task: Fix persisted public session lookup for Drive shared and public bookmarks.
Status: Updated the lookup to return `number | null`, accept only numeric `ps-` keys, preserve ID 0, and avoid storage writes. The bookmark hook now resumes only when an ID exists and restores the saved key password before listing bookmarks.
Verification: Focused Drive Jest suites passed (2 suites, 17 tests); `git diff --check` passed.
