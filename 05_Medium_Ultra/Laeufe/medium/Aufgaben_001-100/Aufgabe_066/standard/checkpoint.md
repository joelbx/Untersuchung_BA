Task: replace inline height values containing vh with auto in mail HTML preparation.
Status: complete. Added transformStyleAttributes and invoked it after transformStylesheet, before transformRemote. Added test covering root and descendants, !important, and unaffected styles.
Verification: Jest with coverage disabled passed transformRemote and transformStyleAttributes suites (5 tests); Prettier and git diff --check passed.
Constraints: edited checked-out files only; git history/index/harness configuration untouched.
