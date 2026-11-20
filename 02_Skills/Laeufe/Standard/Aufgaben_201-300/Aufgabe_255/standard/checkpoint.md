# Checkpoint

Task: fix password lookup inline key=value options, chars input formats, and deterministic seed behavior.

Implemented in `lib/ansible/plugins/lookup/password.py`: moved `_parse_parameters` into `LookupModule`, initialized plugin options before parsing, read defaults with `get_option`, retained path reconstruction and key validation, and parsed string `chars` while preserving list input. Changed `chars` option type to `raw` so the normal plugin loader accepts lists.

Updated `test/units/plugins/lookup/test_password.py` for instance parsing, option precedence, string and list chars, and seeded output through the actual plugin loader.

Checks: `PYTHONPATH=lib:test/units python -m pytest -q --reruns 0 test/units/plugins/lookup/test_password.py` passed (33 tests). `git diff --check` passed. Initial test attempts failed because direct plugin construction in the existing fixture lacked loader registered options; the fixture was updated and the suite then passed. No remaining check uncertainty.
