Implemented the atomic move permission fix. Newly created files use `0o0600 & ~umask`; modules that accept `mode` and omit it track created paths and receive the specified warning during result formatting. Applying a mode clears that path from tracking.

Validation passed: 63 relevant tests, and `git diff --check`.