# Checkpoint

Task: Make GuiProcess report stdout and stderr live and publish ordered, severity-aware final summaries only for nonempty streams.

Status: Investigating root cause and tests. `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find.

Root cause: QProcess is fixed to StandardOutput and only generic readyRead is connected. The live handler reads via readLine from that channel and unconditionally emits an info message, even when empty. StandardError is read only by _on_finished. Qt has per-stream readyReadStandardOutput/StandardError signals and readAllStandardOutput/readAllStandardError methods already used at finish.

Reproduction: `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/misc/test_guiprocess.py -k test_live_output_and_final_summaries` failed for stderr-only and dual-stream cases: no error message within 500 ms while child remained alive. Existing tests show stdout live and final output, stderr only at finish. Hypothesis: using per-stream signals and stream-specific reads, then draining both at finish before ordered summaries, resolves both defects.

Implementation: Connected per-stream QProcess ready signals, reads each stream into its own buffer, emits live info/error only when data arrives, and drains both buffers before final stdout-then-stderr summaries. The stderr summary uses error severity and the same replace key as live stderr.

Verification: `QT_QPA_PLATFORM=offscreen python -m pytest -q -o addopts='' tests/unit/misc/test_guiprocess.py tests/unit/misc/test_editor.py tests/unit/commands/test_userscripts.py` exited 0: 107 passed, 4 skipped. `git diff --check` exited 0. No offline tooling blocker affected verification.
