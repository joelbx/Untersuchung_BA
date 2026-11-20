# Checkpoint

Issue: deterministic and narrowly scoped no_log sanitization.

Implemented:
- `remove_values` masks sensitive substrings in string values only, preserves mapping keys and scalar values, preserves container classes, and traverses iteratively.
- Added public `sanitize_keys` with recursive mapping-key masking, exact-key sentinel replacement, `_ansible` and caller-provided ignore handling.
- Added URI response sanitization guarded by `module.no_log_values`, with `NO_MODIFY_KEYS`.
- Kept JSON output compatible with preserved `datetime.date` values by serializing them as ISO dates.
- Updated unit coverage for the changed contract.

Verification:
- Focused `test_exit_json.py`, `test_no_log.py`, and `test_heuristic_log_sanitize.py`: 32 passed.
- `py_compile` and `git diff --check`: passed.
- Full `test/units/module_utils/basic`: 22 failures, 272 passed, 14 skipped. Failures show warning/deprecation state leaking across tests (the first failure sees warnings left by earlier argument-spec tests, followed by warning/deprecation output in subsequent tests). The focused files pass in isolation.
