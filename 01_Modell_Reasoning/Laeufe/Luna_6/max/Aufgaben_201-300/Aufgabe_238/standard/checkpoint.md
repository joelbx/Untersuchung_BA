# Checkpoint: replace deprecated `:buffer` user interface

Repository: `/app`

## Objective
Make `:tab-select` the registered, documented, and completable public command for selecting tabs; expose `tabs` and `other_tabs` completion providers; remove stale active `:buffer` references.

## Changes made
- Renamed the command to `tab-select` and removed the `buffer` command registration.
- Renamed tab completion providers to `tabs` and `other_tabs`; updated tab-select and tab-take to use them.
- Kept numeric index, substring URL/title matching, `win_id/index`, count precedence, and window activation behavior in the renamed command.
- Updated the `gt` default binding, manual completion note, completion references, and tab selection scenarios to use `:tab-select`.
- Regenerated the command and settings help from source metadata. The generated command index and usage now list `tab-select` and omit `buffer`.

## Verification
- `pytest -q tests/unit/completion/test_models.py`: 73 passed.
- `pytest -q tests/end2end/features/test_tabs_bdd.py -k tabselect`: 11 failed during application startup and 1 skipped. The harness forces QtWebKit, which cannot be imported in this environment (`PyQt5.QtWebKit` is unavailable); the failures occur before command execution.
- `git diff --check`: passed.
- Active source, help, and test references to `:buffer`, `miscmodels.buffer`, and `other_buffer` were searched; none remain. Historical changelog entries were preserved.

## Current status
Implementation and review are complete. The end-to-end limitation is environmental; no harness configuration was changed.
