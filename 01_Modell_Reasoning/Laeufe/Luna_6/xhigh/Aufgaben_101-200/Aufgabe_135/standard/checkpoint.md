# Checkpoint

Task: update Ansible's `min` and `max` filters to forward Jinja2 enhanced-filter keyword arguments when available, retain built-in fallback for positional-only calls, and raise the specified `AnsibleFilterError` when keyword arguments are unsupported.

Implementation location: `lib/ansible/plugins/filter/mathstuff.py`.

Findings: Jinja2 2.11.2 is installed and provides both enhanced filters. Existing unit tests call `min`/`max` directly; they now pass the Jinja environment because these filters are required to use `@environmentfilter`.

Changes made: added independent optional imports for `do_min` and `do_max`; each filter forwards all keyword arguments when its Jinja implementation is available and otherwise raises the specified `AnsibleFilterError` for keyword arguments while retaining the Python built-in fallback without them.

Validation: direct focused pytest run passed all 49 tests. `ansible-test units test/units/plugins/filter/test_mathstuff.py` could not run because its Python 3.8 isolated interpreter does not have pytest installed.
