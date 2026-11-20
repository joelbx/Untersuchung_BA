# Checkpoint

Implemented in `qutebrowser/browser/webkit/certificateerror.py`:
- Accept optional `reply` and `errors` constructor parameters, while retaining the legacy positional errors sequence.
- Keep reply handling passive during wrapper construction/rendering.
- Render a single error as an escaped paragraph and multiple errors as an escaped unordered list.

Verification: `pytest -q tests/unit/browser/webkit/test_certificateerror.py` passed (4 tests); `python -m compileall -q qutebrowser/browser/webkit/certificateerror.py` passed.
