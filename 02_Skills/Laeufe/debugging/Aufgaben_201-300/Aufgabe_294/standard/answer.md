Updated collection build and install to preserve internal file and directory symlinks, keep external file links as regular files, and validate extraction paths. Tar extract helpers now return both `TarInfo` and a readable stream.

The regression tests failed before the fix and pass now. Final checks: **103 tests passed**; `git diff --check` passed.