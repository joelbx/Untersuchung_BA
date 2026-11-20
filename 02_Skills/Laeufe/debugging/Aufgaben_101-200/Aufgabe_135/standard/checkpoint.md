# Checkpoint

Task: support Jinja2 keyword arguments in mathstuff min/max with built-in fallback.
Status: investigating root cause and local tests.

## Investigation
- Baseline `PYTHONPATH=lib python -m pytest -q test/units/plugins/filter/test_mathstuff.py`: 49 passed.
- `mathstuff.min/max` accept only the sequence and call built-ins. Thus Jinja2 keyword arguments fail at the filter signature before Jinja2 can perform attribute/case-sensitive selection.
- Local Jinja2 2.11.2 exposes `do_min/do_max(environment, value, case_sensitive=False, attribute=None)`; `unique` in this module demonstrates optional Jinja2 dispatch and environment injection.
- Hypothesis: using environment-filter wrappers and forwarding `**kwargs` to the corresponding Jinja2 function fixes the issue; when unavailable, reject kwargs and use built-ins for plain calls.

## Resolution
- Added separate optional imports for Jinja2 `do_min` and `do_max`.
- Decorated Ansible min/max with `@environmentfilter`, forwarded every keyword to Jinja2 when available, and retained built-in fallback with the required keyword error.
- Added regression tests for attribute selection, case sensitivity, fallback behavior, and Jinja2 template rendering.
- Pre-fix focused reproduction failed with expected signature/keyword errors (6 tests failed).
- Final `PYTHONPATH=lib python -m pytest -q test/units/plugins/filter/test_mathstuff.py`: 54 passed, exit 0.
- Final `git diff --check`: exit 0.
