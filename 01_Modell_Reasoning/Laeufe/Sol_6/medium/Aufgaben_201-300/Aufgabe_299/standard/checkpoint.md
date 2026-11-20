# Checkpoint

Task: Add filesystem path completion to `:open`.
Status: Implemented and reviewed.
Changes: Added `FilePathCategory`; integrated it into URL completion; added `completion.favorite_paths` and enabled `filesystem` by default in `completion.open_categories`; updated user help and tests.
Verification: 99 relevant unit tests passed (2 benchmarks deselected). Pytest process reports an X11 connection error during teardown after the passing summary. `git diff --check` passed.
