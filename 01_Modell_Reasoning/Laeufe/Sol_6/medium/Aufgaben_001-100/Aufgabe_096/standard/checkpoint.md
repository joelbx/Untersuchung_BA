Task: Fix atomic_move default permissions and warning tracking in module_utils/basic.
Status: Implemented restrictive default permissions, per-module created-file tracking, warning emission, and explicit-mode removal. Added atomic move tests.
Validation: 47 targeted tests passed; git diff --check passed. Full module_utils/basic run had unrelated warning-global-state test isolation failures (22 failed, 277 passed, 14 skipped); deprecation warning failure reproduced without the atomic move tests.
