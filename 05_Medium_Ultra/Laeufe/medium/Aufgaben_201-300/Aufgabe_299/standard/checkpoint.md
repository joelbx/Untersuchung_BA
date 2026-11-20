# Checkpoint

Task: Add filesystem path completion for `:open`.
Status: Implemented and locally verified.

Changes:
- Added `FilePathCategory` with favorites, absolute paths, local file URLs, and tilde expansion.
- Registered the category in the URL completion model, with configurable order.
- Added `completion.favorite_paths` and documented both settings in help.
- Added and adjusted completion tests.

Verification: 101 selected completion/config tests passed; pytest reported an X11 teardown error after the pass summary (exit status 1). `git diff --check` passed.
