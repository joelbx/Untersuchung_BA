Updated the repository so both `safe_eval` entry points emit an Ansible runtime deprecation notice for 2.21. `check_type_dict` now parses JSON, dictionary literals, and `key=value` pairs without calling `safe_eval`, and raises `TypeError` for malformed input. Added the changelog entry and tests.

Verification: 118 relevant tests passed; `git diff --check` passed.