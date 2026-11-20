# Checkpoint

Task: fix `GUIProcess` so stdout and stderr stream live, with ordered and severity-specific final summaries only for streams containing output.

Implemented separate Qt ready-read handlers for standard output and standard error. Both streams are drained and accumulated independently; live updates are emitted only for non-empty data when output messages are enabled. Completion drains pending bytes and publishes stdout's informational summary before stderr's error summary, omitting summaries for empty streams.

Updated focused unit coverage to account for both live updates and summaries, and added a test that confirms stderr becomes visible while the process is still running.

Verification: `pytest -q tests/unit/misc/test_guiprocess.py` passed (41 passed); `git diff --check` passed.
