Deprecated both `safe_eval` entry points with a runtime notice targeting 2.21 and added a changelog entry. `check_type_dict` now parses JSON, dictionary literals, and `key=value` pairs without calling `safe_eval`; it rejects non-dictionaries and malformed input with `TypeError`.

The relevant local suite passed: **91 tests**. `git diff --check` passed.