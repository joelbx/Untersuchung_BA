Task: add `flipt.is_auth_method` Rego built-in for readable authentication method names.
Status: implemented and registered the built-in for local and bundle engines; added focused mapping and policy evaluation tests. Relevant engine tests pass and `git diff --check` is clean.
Constraint: local repository and existing tests only; leave git history, index, and harness untouched.
