Implemented the atomic move permission fix. New files now use `0o0600 & ~umask`; when a module supports `mode` and the user omits it, created paths are tracked and warned about during result formatting. Applying an explicit mode clears that path from tracking.

The focused existing tests passed: **63 passed**. `git diff --check` passed.