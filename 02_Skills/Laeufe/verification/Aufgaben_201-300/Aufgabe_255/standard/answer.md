Updated the password lookup to apply key=value parameters, use term values ahead of plugin defaults, and generate repeatable output for a fixed seed. `chars` now accepts a list or a comma-separated string, including `,,` for a literal comma.

Verification: all 41 lookup unit tests passed; `git diff --check` passed.