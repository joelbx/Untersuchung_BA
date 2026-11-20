# Checkpoint

Task: predictable `no_log` value and key sanitization.

Root cause: `remove_values` traversed and redacted mapping keys, converted exact string and numeric matches to a sentinel, converted dates, and rebuilt tuples as lists. `uri` did not sanitize response keys. Existing JSON fallback handled `datetime` but not `date`, which became visible when dates stopped being converted by `remove_values`.

Implementation: iterative postorder container traversal; value-only `remove_values`; public `sanitize_keys` with exact-key sentinel, substring masking, ignored keys and `_ansible` exemption; `uri` conditional invocation with `NO_MODIFY_KEYS`; JSON date fallback. Updated legacy tests and added focused tests.

Checks: `PYTHONPATH=lib:test python -m pytest -q test/units/module_utils/basic/test_exit_json.py test/units/module_utils/basic/test_no_log.py test/units/module_utils/basic/test_no_log_sanitization.py test/units/module_utils/basic/test_heuristic_log_sanitize.py` passed (35 passed). `git diff --check` passed.

Broader check: `PYTHONPATH=lib:test python -m pytest -q test/units/module_utils/basic` failed (22 failed, 275 passed, 14 skipped). The first run was before fixing date serialization and updating exit_json expectations. Other failures in `test_argument_spec.py` and `test_deprecate_warn.py` concern global warning state retained between tests; rerunning `test_deprecate_warn.py test_argument_spec.py -x` separately reproduced that warning-state failure. Relevant exit_json tests subsequently passed in isolation. No claim that the full basic suite passes.
