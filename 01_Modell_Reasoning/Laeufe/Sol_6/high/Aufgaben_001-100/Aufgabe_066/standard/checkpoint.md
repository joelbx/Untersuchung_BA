Task: normalize inline height values using vh in mail HTML preparation.
Status: complete. Added transformStyleAttributes, invoked it after transformStylesheet and before transformRemote. The transform covers the root and styled descendants, preserves other inline declarations (including proton-url), and retains !important.
Verification: targeted Jest transformStyleAttributes and transformRemote suites passed (7 tests); targeted ESLint passed; git diff --check passed.
Constraints observed: local repository only; no git history, index baseline, or harness configuration changes.
