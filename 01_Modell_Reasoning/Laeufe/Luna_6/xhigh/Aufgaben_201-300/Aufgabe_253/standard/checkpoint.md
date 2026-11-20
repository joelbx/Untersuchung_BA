# Checkpoint

## Issue
`GuiProcess` should stream both stdout and stderr while running, then publish a nonempty final summary per stream. Stdout summaries must be informational and precede stderr summaries; stderr summaries must use error severity.

## Investigation
- Located the checked-out repository at `/app`.
- `rg` is unavailable in this environment; proceeding with targeted `find`/`grep` searches.

## Plan
1. Find `GuiProcess` and its existing tests.
2. Update stream handling and final reporting while preserving interfaces.
3. Run the relevant existing tests and record results.

## Implementation progress
- Connected `GUIProcess` to separate `readyReadStandardOutput` and `readyReadStandardError` signals.
- Added per-stream live updates; nonempty stdout uses info severity and nonempty stderr uses error severity.
- Completion drains both streams and publishes final stdout then final stderr, skipping streams with no buffered output.
- Updated the existing `GUIProcess` output-message test expectations for live stderr and ordered final summaries.

## Validation
- Relevant unit tests are next: `tests/unit/misc/test_guiprocess.py`.

## Validation results
- `python -m pytest tests/unit/misc/test_guiprocess.py -q`: 40 passed.
- `git diff --check`: passed.

## Final state
- Both output streams have independent live message handling.
- Final stream summaries are emitted only for nonempty buffers, stdout first as info and stderr second as error.
