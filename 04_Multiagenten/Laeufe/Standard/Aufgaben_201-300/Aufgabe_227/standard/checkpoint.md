# Checkpoint

Task: Gate the MIME suffix workaround using runtime Qt only.

Changes:
- Both workaround bounds call version_check with compiled=False.
- Documented the compiled parameter and changed compiled=True plus exact=True to raise RuntimeError.
- Added regression coverage for runtime 6.2.2, 6.2.3, 6.6.9, and 6.7.0 with divergent compiled versions.

Verification:
- Focused version and suffix tests: 35 passed.
- Full affected test modules: 197 passed, 2 unrelated failures under Qt 6.9.1 (QDataStream status count now 5; QSaveFile warning emitted).
- git diff --check passed.
