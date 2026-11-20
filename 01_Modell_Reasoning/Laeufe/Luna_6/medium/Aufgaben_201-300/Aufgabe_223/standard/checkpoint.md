# Checkpoint

Issue: preserve module-declared shebang interpreters and arguments during new-style module processing, while honoring explicit interpreter overrides and retaining the default when no interpreter is available.

Progress: locating implementation and existing tests.

Implementation: `_extract_interpreter` now parses first-line shebangs with `shlex.split`; `_get_shebang` returns a complete shebang and keeps declared interpreter arguments; module preparation resolves against the module's own interpreter and changes the line only when the interpreter differs. Python configuration/discovery is applied to versioned Python paths as well. Updated the legacy unit expectation for the new always-return-a-shebang contract.

Verification: `python -m pytest -q test/units/executor/module_common/test_module_common.py` passed (38 tests); `git diff --check` passed.
