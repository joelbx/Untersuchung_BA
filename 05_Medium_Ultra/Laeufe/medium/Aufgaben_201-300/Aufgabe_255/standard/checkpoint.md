Task: Fix password lookup key=value parameter parsing, chars handling, and seeded determinism.
Status: Complete. Moved parameter parsing into LookupModule, sourced defaults from plugin options after set_options, accepted string and list chars, and preserved inline precedence/path validation.
Verification: python -m pytest test/units/plugins/lookup/test_password.py -q --disable-warnings (33 passed); git diff --check passed.
Changed: lib/ansible/plugins/lookup/password.py and test/units/plugins/lookup/test_password.py.
Constraints observed: Local code and tests only; git history, index baseline, and harness configuration unchanged.
