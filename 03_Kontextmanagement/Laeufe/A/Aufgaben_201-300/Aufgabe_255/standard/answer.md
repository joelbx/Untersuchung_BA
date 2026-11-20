Fixed the password lookup so inline key=value parameters, including `seed`, take precedence over plugin defaults. `chars` now accepts a list or a comma-separated string, with `,,` preserved as a literal comma.

The password lookup unit suite passes: **35 tests**. `git diff --check` also passes.