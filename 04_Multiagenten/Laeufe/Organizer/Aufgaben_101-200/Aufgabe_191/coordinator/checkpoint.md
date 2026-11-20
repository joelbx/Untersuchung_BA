Task: Add registration token support to InteractiveAuth for stable and unstable stages.
Status: Implemented token entry, stage mapping, translations and focused tests.
Verification: Focused Jest suite passed (4 tests); ESLint and Prettier passed; git diff --check passed. Full type lint fails in pre-existing SlidingSync files, with no errors in changed files.
Delegation: None.
