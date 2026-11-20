Task: Fix qutebrowser GUI process startup error messages.
Status: Complete. Updated _on_error to show capitalized process name, quoted command, error-specific wording and detail; missing executable/permission hints on non-Windows. Added process error tests.
Verification: pytest -o addopts='' -q tests/unit/misc/test_guiprocess.py (30 passed); git diff --check passed.
