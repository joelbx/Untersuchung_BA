# Checkpoint

Implemented undefined-value handling for YAML dumping. `AnsibleDumper` now invokes `bool(data)` for `AnsibleUndefined`, allowing StrictUndefined to raise its original undefined error. Both YAML filters wrap dump failures in filter-specific `AnsibleFilterError` instances and retain the original exception in `orig_exc`. The templating layer recognizes wrapped Jinja undefined errors and raises `AnsibleUndefinedVariable` with the underlying cause retained.

Verification: `python -m pytest -q test/units/plugins/filter/test_core.py test/units/parsing/yaml/test_dumper.py` (11 passed); manual undefined propagation checks passed; `git diff --check` passed.
