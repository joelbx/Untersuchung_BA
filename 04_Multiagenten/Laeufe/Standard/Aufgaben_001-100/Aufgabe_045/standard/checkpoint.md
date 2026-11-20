Task: fix collection FQCN validation so Python keywords in either segment are rejected.
Status: implementation complete and focused tests pass.
Changes: collection loader now validates both name segments as Python identifiers excluding keywords; galaxy requirement parsing uses that validator; legacy dataclasses helpers and their Python 2/3 compatibility branch removed; collection reference validation also checks the collection name.
Verification: collection-loader unit file 73 passed; targeted galaxy CLI tests 17 passed, run in separate processes because the loader test file tears down global finder state; git diff --check passed.
Constraints observed: local code/tests only; git history, index, and harness configuration unchanged.
