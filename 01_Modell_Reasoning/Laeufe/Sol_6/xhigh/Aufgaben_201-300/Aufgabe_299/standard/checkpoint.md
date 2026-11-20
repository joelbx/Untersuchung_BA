Task: Add filesystem path completion to :open.
Status: Complete.
Changes: Added FilePathCategory for absolute, file:/// and ~ paths; integrated configurable Filesystem category; added completion.favorite_paths; regenerated settings help; added and updated completion tests.
Verification: Controlled Xvfb run of tests/unit/completion and tests/unit/config/test_configdata.py: 321 passed, 1 skipped, 1 xfailed. Focused rerun after final edit: 102 passed. git diff --check clean.
