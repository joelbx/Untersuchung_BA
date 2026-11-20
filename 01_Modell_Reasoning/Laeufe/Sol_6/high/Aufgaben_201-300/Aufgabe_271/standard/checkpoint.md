Task: Fix IA ImportAPI publisher/location parsing and ISBN classification.
Status: Implementation complete. IA publisher parsing now handles ordered locations and publishers, brackets, unidentified places, malformed extra colons, and comma fallback. ISBN classification moved to openlibrary.utils.isbn and remains length based. Added focused tests.
Verification: 64 tests passed across ImportAPI, upstream utils, and ISBN test modules. git diff --check passed. Black is unavailable in the environment.
Constraints: Use local code/tests only; preserve git history, index, and harness configuration.
