Updated module preparation to honor a new-style Python module’s shebang and arguments. Explicit interpreter overrides still take precedence; new-style modules without a shebang use `/usr/bin/python`. Shebang replacement now preserves the original argument text, and the encoding line follows the shebang.

The focused tests passed: **49 passed**. `git diff --check` passed. No delegation was used.