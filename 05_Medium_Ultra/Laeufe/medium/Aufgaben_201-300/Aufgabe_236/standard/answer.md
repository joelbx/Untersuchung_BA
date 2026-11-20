Deprecated both `safe_eval` entry points with a runtime notice targeting 2.21. `check_type_dict` now parses JSON, dictionary literals, and validated `key=value` pairs without calling `safe_eval`; malformed inputs raise `TypeError`. Added a changelog entry and tests.

Verification: 90 relevant tests passed, and `git diff --check` passed.