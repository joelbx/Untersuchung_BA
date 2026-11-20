# Checkpoint

Task: raise controller minimum to Python 3.12, remove obsolete controller compatibility code, update metadata, tests and changelog.
Status: edits complete. Collection extraction and loader tests: 73 passed, 1 skipped on Python 3.11. CLI and ansible-test both reject Python 3.11 with the same message. Role install tests cannot collect on this host because its Python 3.11 is below the new minimum. No delegation used.
