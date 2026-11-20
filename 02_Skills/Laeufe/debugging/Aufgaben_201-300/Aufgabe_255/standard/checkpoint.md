# Password lookup debugging checkpoint

Investigating parameter parsing and option precedence in `lib/ansible/plugins/lookup/password.py`. No changes to plugin behavior yet.

Baseline: `PYTHONPATH=lib:test/units python -m pytest -q test/units/plugins/lookup/test_password.py` passed (29 tests). The global parser reads `kwargs` directly, while other lookups call `set_options` and read with `get_option`. Its `chars` handling calls `.replace()` on a nonempty value, which fails for list options. Inline `seed` already reaches `random_password` in the current code; the reproducible gap is option handling and list compatibility, so parsing will be moved into the instance while retaining inline precedence.

Regression test failed before fix with `AttributeError: 'list' object has no attribute 'replace'`. After moving parsing, tests that construct the class directly exposed that configured options need a loader-created instance; plugin option definitions were absent on those direct instances. A loader-created instance showed `chars` is declared `type: string`, which rejects lists in `set_options`; the option must permit both types.

Final implementation: parsing is an instance method, `run()` configures options before parsing, inline values override configured defaults, `chars` uses string splitting only for strings and preserves lists. The `chars` option now has `type: raw` so Ansible accepts lists. Existing candidate-character expansion remains in place.

Checks passed:
- `PYTHONPATH=lib:test python -m pytest -q test/units/plugins/lookup/test_password.py --reruns 0` (34 passed).
- `ANSIBLE_ROLES_PATH=../ PYTHONPATH=/app/lib /app/bin/ansible-playbook runme.yml -i localhost, -c local -e output_dir=/tmp/lookup-password-codex` from `test/integration/targets/lookup_password` (31 tasks passed; inline and keyword seed checks included).
- `git diff --check` (no errors).
