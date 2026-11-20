# Collection symlink support

Implemented internal symlink preservation in collection tar builds, single-entry directory symlink manifests, child-path validation, tuple-returning tar extract helpers, and safe symlink restoration during artifact installs. Updated collection unit tests and added build/install round trip and unsafe link checks. Verification complete: 104 focused unit tests passed, changed files compiled, and `git diff --check` passed.
