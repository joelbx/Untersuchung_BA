Fixed `atomic_move()` so newly created files receive `0600` permissions under a `0022` umask. When a module accepts `mode` but it is omitted, the module now tracks each created path and emits the required warning during result formatting. A later call to `set_mode_if_different()` with a mode removes that path from warning tracking.

Added focused tests in [test_atomic_move.py](/app/test/units/module_utils/basic/test_atomic_move.py). A native subagent added the tests, and another reviewed the implementation.

Validation: the `basic` unit suite passed with test isolation (`301 passed, 14 skipped`); `git diff --check` passed. The unforked suite has order-dependent failures caused by shared warning and deprecation state.