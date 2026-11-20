# Checkpoint

Task: fix MIME suffix workaround version gating so it consults runtime Qt only, and clarify the compatibility utility's `compiled` parameter.

Completed:
- MIME suffix bounds now call `version_check("6.2.3", compiled=False)` and `version_check("6.7.0", compiled=False)`.
- `version_check` documentation describes runtime-only behavior; ambiguous `compiled=True, exact=True` now raises `RuntimeError`.
- Existing tests were adjusted to assert the explicit runtime-only flag and exception type.

Verification:
- `pytest -q tests/unit/utils/test_qtutils.py::test_version_check tests/unit/utils/test_qtutils.py::test_version_check_compiled_and_exact`: 13 passed.
- `pytest -q tests/unit/browser/webengine/test_webview.py::test_suffixes_workaround_extras_returned`: 7 passed.
- `git diff --check`: passed.
- Broader relevant test runs hit unrelated environment failures: `test_qdatastream_status_count` expects four enum values but installed Qt exposes five; pytest then aborts while initializing its Qt fixture. The MIME extra-suffix tests passed before that abort.
