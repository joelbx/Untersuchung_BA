Task: Add filesystem path completion to :open.
Status: Implemented and verified.
Changes: Added FilePathCategory, registered it in URL completion, added completion.favorite_paths and filesystem open category config, updated help and unit tests.
Verification: 68 completion tests passed (benchmark excluded in final focused run); 31 configdata tests passed; git diff --check passed.
Constraints observed: Local repository/tests only; git history, index baseline, and harness configuration untouched.
