Fixed the [password lookup plugin](/app/lib/ansible/plugins/lookup/password.py). Inline `key=value` options now take precedence over plugin defaults, seeded lookups are deterministic, and `chars` accepts lists or comma-separated strings with `,,` for a literal comma.

Updated the [existing tests](/app/test/units/plugins/lookup/test_password.py): **33 passed**. `git diff --check` passed.