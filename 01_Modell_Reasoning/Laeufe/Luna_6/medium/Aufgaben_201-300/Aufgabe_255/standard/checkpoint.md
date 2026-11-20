# Checkpoint

Task: fix password lookup key=value parameter parsing and `chars` handling.

Initial inspection: implementation is in `lib/ansible/plugins/lookup/password.py`; unit coverage is in `test/units/plugins/lookup/test_password.py`.

Next: inspect the plugin and tests, implement the requested parsing behavior, and run the focused existing unit tests.
