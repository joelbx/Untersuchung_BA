# Checkpoint

Issue: Undefined values passed to YAML filters raised a PyYAML representation error.

Completed:
- Registered an AnsibleUndefined representer that evaluates bool(data), surfacing Jinja's undefined-variable error.
- Wrapped dump failures in to_yaml and to_nice_yaml with filter-specific AnsibleFilterError messages and orig_exc.
- Added direct dumper, filter, and template regression coverage.

Verification: PYTHONPATH=lib:test pytest -q test/units/parsing/yaml/test_dumper.py test/units/plugins/filter/test_core.py test/units/template/test_templar.py (64 passed); git diff --check passed.
