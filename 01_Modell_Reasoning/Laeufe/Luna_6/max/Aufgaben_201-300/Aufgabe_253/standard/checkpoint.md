# Checkpoint

Task: Fix `GuiProcess` so stdout and stderr are surfaced live and produce ordered, severity-appropriate final summaries only when they contain output.

Implemented in `qutebrowser/misc/guiprocess.py`: connected the channel-specific QProcess ready signals, stream both channels as they arrive, retain separate replace IDs, and publish final summaries in stdout-then-stderr order only for nonempty streams. Extended focused tests for stderr live updates, message severity, empty streams, and final ordering.

Verification: `pytest -q --tb=short tests/unit/misc/test_guiprocess.py` passed (45 passed). `git diff --check` passed.
