Updated `safe_eval` in both the global function and `AnsibleModule` wrapper to emit a deprecation warning for target version 2.21. Added a changelog entry for both APIs.

`check_type_dict` now tries JSON, then safe literal parsing, then key/value pairs. It returns only dictionaries and raises descriptive `TypeError`s for malformed inputs. It no longer calls `safe_eval`.

Validation: the existing dictionary parsing and `safe_eval` tests passed (24 tests).