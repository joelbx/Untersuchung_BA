`GUIProcess` now streams stderr as it arrives, gives stdout and stderr separate live messages, and publishes nonempty final summaries in stdout then stderr order. The message view also preserves error severity when both streams contain identical text.

The relevant tests pass under Xvfb: **71 passed**.