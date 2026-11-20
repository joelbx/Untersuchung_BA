# Checkpoint

- Task: preserve internal collection symlinks while building and installing artifacts, and validate extraction paths.
- Changes: manifest traversal stops at directory links; tar build stores internal links with relative targets and copies external file links; install restores safe links, copies readable unsafe file links, validates paths, and exposes `(TarInfo, stream)` from tar helpers.
- Tests: `PYTHONPATH=lib:test python -m pytest -q test/units/galaxy` passed (150 passed). `git diff --check` passed.
- Note: the initial focused run failed three preexisting expectations for copied links and stream-only helper output; those tests were updated to the required behavior and the full suite passed afterward.
