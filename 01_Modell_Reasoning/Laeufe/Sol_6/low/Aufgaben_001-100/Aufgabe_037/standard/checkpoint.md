Task: Fix undefined values passed through YAML filters.
Status: Implemented and verified.
Changes: AnsibleDumper represents AnsibleUndefined by evaluating its boolean value, causing Jinja's UndefinedError. Both YAML filters wrap failures in AnsibleFilterError with filter name and orig_exc. Added regression tests for nested undefined values and supported values.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/parsing/yaml/test_dumper.py test/units/plugins/filter/test_core.py (16 passed).
