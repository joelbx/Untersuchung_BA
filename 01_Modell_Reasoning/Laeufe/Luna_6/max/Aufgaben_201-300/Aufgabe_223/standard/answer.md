Updated module handling to extract the source shebang and its arguments, preserve them by default, and honor explicit interpreter overrides. Modules without a shebang receive the default Python interpreter; existing shebangs are rewritten only when the resolved interpreter differs. The encoding line is placed immediately after the shebang.

Updated the existing `_get_shebang` test for its complete shebang return value.

**Verification:** 61 targeted unit tests passed, including module-common, interpreter-discovery, and action tests. `git diff --check` passed.