# Debugging checkpoint

Task: resolve reported sentinel, module, YAML, templar, lookup, CLI, deprecation, and timedout behaviors.

Status: investigating local code and tests. No fixes attempted.

## Root cause and hypothesis
- Reproduction: `python /tmp/ansible_issue_repro.py` exits 1 at `_AnsibleMapping()` with missing `value` TypeError. Direct Templar probe raises TemplateOverrides NoneType TypeError.
- YAML compatibility wrappers require a positional value and discard base constructor keyword patterns.
- Templar merges None override values into validated `TemplateOverrides`; both entry points need to filter them.
- `timedout` returns the raw `period` value, so result can be int or other truthy object.
- Lookup error branch builds distinct verbose messages and wraps non-warn exceptions; warn/ignore need common context and other modes should propagate.
- Deprecation display path `_deprecated` lacks a config guard and sends disablement advice as an independent normal warning; module result deprecations go through that path.
- CLI early setup exception handler uses `str(ex)` and traceback, omitting AnsibleError help text.
- Sentinel use in relevant parameter paths is `Ellipsis`, conflating user values and omitted values.
Hypothesis: changing the source boundary in each path as described above resolves the behaviors without changing other flows.

## Verification note
`python -m pytest -q test/units/module_utils/basic/test_exit_json.py test/units/utils/test_display.py test/units/_internal/templating/test_jinja_plugins.py test/units/errors` failed 2 existing `test_warn_success` cases: `eaw.call_args` was None. Isolation: `python -m pytest -q test/units/errors` passed (65 tests); `python -m pytest -q test/units/utils/test_display.py test/units/errors/test_handler.py -k 'not test_deprecation_configuration_and_message'` still failed the same 2 cases. This appears to be display fixture/order interference, unrelated to the new test; uncertainty remains for combined ordering.

## Final verification
- `python /tmp/ansible_issue_repro.py`: passed after patch (was failing before patch).
- `python -m pytest -q test/units/parsing/yaml/test_objects.py test/units/template/test_template.py test/units/plugins/test/test_core.py test/units/module_utils/basic/test_exit_json.py test/units/utils/test_display.py test/units/_internal/templating/test_jinja_plugins.py`: 145 passed, 1 skipped.
- `python -m pytest -q test/units/errors`: 65 passed.
- `git diff --check` and `python -m compileall -q` on modified library files: passed.
- Combined display and error handler tests remain order-dependent as documented above; no evidence this patch caused it because excluding the new display test retained the failure.
