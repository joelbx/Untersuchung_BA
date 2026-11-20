Task: Preserve internal collection symlinks during build/install and make tar extraction safe.
Status: Implemented and verified. Manifest records internal symlink directories once; build stores relative symlinks and dereferences external file links; install validates paths and restores safe symlinks. Tar helpers yield member plus stream.
Verification: test/units/galaxy/test_collection.py: 63 passed. Adjacent CLI suite: 126 passed, 4 warning-count assertion failures in test/units/cli/test_galaxy.py (tests mock install_collections and do not exercise modified collection code). git diff --check passed.
Constraints: Local code/tests only; no git history, index baseline, or harness changes.
Focused test/units/cli/galaxy suite: 19 passed.
