Deprecated both `safe_eval` entry points with a runtime deprecation notice targeting 2.21 and added changelog entries. `check_type_dict` now parses JSON, dictionary literals, and `key=value` pairs without calling `safe_eval`; malformed or non-dictionary input raises `TypeError`.

Verification: 92 relevant tests passed, and `git diff --check` passed.