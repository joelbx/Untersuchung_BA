`GUIProcess` now shows stderr output while the process is running. At completion, it publishes a summary for each stream that produced output: stdout as info, then stderr as error. Empty streams produce no messages.

The relevant tests passed: 46 `GUIProcess` tests, plus 65 editor and userscript tests (4 skipped).