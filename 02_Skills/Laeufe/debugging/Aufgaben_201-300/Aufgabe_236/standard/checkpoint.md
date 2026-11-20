# Checkpoint

Task: deprecate `safe_eval`, remove its use from dictionary validation, and verify parsing and warnings.

Status: investigating current implementation and tests. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find`.

## Root cause and hypothesis

`check_type_dict` calls `safe_eval` after a JSON failure for brace-prefixed strings and returns its result without checking that it is a dict. Its separate key=value scanner drops empty tokens and never checks balanced quotes, dangling escapes, or whether every token has a nonempty key and value. `safe_eval` itself never emits Ansible's runtime deprecation record.

Working pattern: `common.process.get_bin_path` calls `common.warnings.deprecate(..., version='2.21', collection_name='ansible.builtin')`. Hypothesis: use that API at the global `safe_eval` entry point; delegate the module wrapper as before. Parse JSON first, then literal dictionaries via `ast.literal_eval`, then validated key=value tokens where appropriate. Reject non-dicts and malformed tokens with TypeError.

## First implementation check

Command: `python -m pytest -q test/units/module_utils/common/validation/test_check_type_dict.py test/units/module_utils/basic/test_safe_eval.py test/units/module_utils/common/parameters/test_list_no_log_values.py test/units/module_utils/common/arg_spec/test_validate_invalid.py`
Result: 4 failed, 48 passed. Three failures share a scanner bookkeeping error: a valid final field after a comma leaves `after_comma` set. One pre-existing test asserts the old generic error text, so keep that text for compatibility. This is a local implementation error, not a new parsing hypothesis.

## Final verification

`python -m pytest -q test/units/module_utils/common/validation test/units/module_utils/common/parameters test/units/module_utils/common/arg_spec test/units/module_utils/basic/test_safe_eval.py` — exit 0, 168 passed.

`git diff --check` — exit 0, no whitespace errors.

Added a regression case for explicitly quoted empty values (`k1=""`), which the previous parser accepted. It failed before the adjustment and passes now. Changelog fragment added for both deprecated entry points. No external tooling was used.
