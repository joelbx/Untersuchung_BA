Fixed both review findings. The kebab menu now aligns with the current-session header’s right edge, and activating an option closes the menu even if that option stops click propagation. Added a regression test for closure and focus restoration.

All 72 relevant Jest tests and 10 snapshots pass. `git diff --check` passes.

**TEST_ENVIRONMENT_PROBLEM:** The TypeScript check still exits with errors in the prepared `matrix-js-sdk` dependency and unrelated app and test files. It reports no errors in the changed files.