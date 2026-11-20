# Checkpoint

Task: Resolve process completion messaging in the Qute browser.

Findings: GUIProcess completion messages lacked the PID; ProcessOutcome treated SIGTERM as a generic crash and did not show signal names.

Changes: Added SIGTERM detection and a terminated state, added signal-aware outcome text, included the PID in completion messages, and suppressed the default SIGTERM completion notification. Updated focused tests for PID references, signal names, and verbose SIGTERM behavior.

Verification: `git diff --check` and `python -m py_compile` pass. The focused pytest suite was attempted, but collection is blocked because PyQt5 is not installed in the checkout environment.

Status: Implementation and regression assertions are complete; final diff review remains.
