Task: Improve Qt wrapper early initialization and error handling.
Status: Implemented early machinery initialization and passed SelectionInfo to Qt availability checker; added NoWrapperAvailableError, autoselection diagnostics, revised string/log output, and updated tests.
Verification: 42 focused Qt/version tests passed; 19 startup tests passed; git diff --check passed. Full test_version.py run stopped during its real Chromium version test in this environment, so targeted version_info was run and passed.
Constraints followed: local code/tests only; git history, index baseline, and harness configuration untouched.
