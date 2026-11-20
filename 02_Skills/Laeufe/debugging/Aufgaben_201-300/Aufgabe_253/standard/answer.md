`GUIProcess` now shows stdout and stderr while the process runs. At completion, it publishes a summary only for each stream with output, with stdout as info before stderr as error.

Added regression coverage for live stderr, final ordering, and empty streams. The relevant tests passed: **107 passed, 4 skipped**.