Deprecated both `safe_eval` entry points with a version 2.21 runtime notice and added a changelog entry. `check_type_dict` now parses JSON, dictionary literals, and validated `key=value` pairs without calling `safe_eval`; malformed or non-dictionary input raises `TypeError`.

Verification: 93 relevant unit tests passed, and `git diff --check` passed.