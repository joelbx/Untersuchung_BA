# Checkpoint

Task: unify specified version parsing with QVersionNumber.
Status: implemented and verified.
Changes: added normalized utils.parse_version; updated Qt checks, early version gate, distribution metadata, crash dialog; updated focused tests.
Verification: 43 focused tests passed; git diff --check passed. Full grouped test run exited early during unrelated test_version cases without a summary.
