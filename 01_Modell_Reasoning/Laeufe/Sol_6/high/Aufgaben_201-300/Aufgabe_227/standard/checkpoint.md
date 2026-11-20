# Checkpoint

Task: Restrict MIME suffix workaround version gating to runtime Qt.

Status: Complete.

Changes:
- Use `compiled=False` for both MIME suffix workaround version bounds.
- Document runtime-only checks and raise `RuntimeError` for `compiled=True` with `exact=True`.
- Add regression tests for runtime bounds with mismatched compiled Qt and PyQt versions.

Verification:
- Focused version-check and suffix-workaround tests: 34 passed.
- Full related modules: 196 passed, 2 unrelated failures on local Qt 6.9.1 (`QDataStream` status count and a `QSaveFile` warning).
- `git diff --check`: passed.
