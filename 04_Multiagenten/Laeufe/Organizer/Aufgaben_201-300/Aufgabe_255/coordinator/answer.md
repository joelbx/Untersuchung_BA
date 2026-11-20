Fixed the password lookup plugin so key=value term parameters are applied, including `seed` for deterministic results. Term values take precedence over plugin options, and `chars` now accepts either a list or a comma separated string with `,,` representing a literal comma.

The password lookup unit suite passes: **33 tests**. `git diff --check` passes. I completed the change without delegation.