Task: Fix IA publisher parsing and ISBN classification for ImportAPI.
Status: Implemented compound publisher parsing, updated ImportAPI to use it, and moved ISBN classification to openlibrary.utils.isbn. Added regression coverage for string/list publishers and parser edge cases.
Verification: 105 passed, 5 xfailed in importapi, upstream, and ISBN test suites; git diff --check passed.
Constraints: Use local code and tests only; keep git history, index baseline, and harness configuration unchanged.
