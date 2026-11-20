Updated `check_type_dict` to parse JSON, safe literals, and validated `key=value` pairs without calling `safe_eval`. Invalid or non-dictionary input now raises a descriptive `TypeError`. Both `safe_eval` entry points are marked deprecated; calls emit Ansible’s runtime deprecation notice for version 2.21. Added a changelog fragment and regression tests.

Verification: 90 relevant tests passed.