Updated collection build and install to preserve internal file and directory symlinks, store external file links as regular files, and validate extraction paths and link targets. The tar helpers now return both the member and its readable stream.

The relevant collection tests passed: **102 passed**. `git diff --check` also passed. No delegation was used.