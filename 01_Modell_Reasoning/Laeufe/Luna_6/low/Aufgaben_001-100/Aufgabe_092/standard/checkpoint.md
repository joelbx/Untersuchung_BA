Task: implement `ansible-galaxy collection install --upgrade/-U` with idempotent constrained upgrades, dependency and prerelease semantics.

Initial plan: inspect CLI argument handling, collection install/resolver code and existing tests; implement behavior and add/update tests; run relevant existing tests.
