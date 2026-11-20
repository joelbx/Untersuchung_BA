Task: Add precise List/Seed typing, normalized subject seed handling, safe helpers, and run relevant existing tests.
Status: complete.
Changes: Added SeedDict and SeedSubjectString typing; normalized key handling for mixed seeds; subject conversion and guard helpers; complete filtered export categories; explicit annotations and safe cover/subject URL handling; focused regression tests.
Validation: 17 list model/plugin tests pass; targeted mypy and Ruff pass; git diff --check passes.
Limit: legacy test_listapi.py cannot collect because it imports unavailable Python 2 cookielib.
Delegation: none.
