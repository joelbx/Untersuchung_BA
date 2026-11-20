Deprecated both `safe_eval` entry points with a runtime notice targeting 2.21. `check_type_dict` now uses JSON, restricted dictionary literals, or `key=value` pairs and raises descriptive `TypeError` messages for invalid input. Added a changelog fragment and focused tests.

Verification: 39 relevant tests passed.