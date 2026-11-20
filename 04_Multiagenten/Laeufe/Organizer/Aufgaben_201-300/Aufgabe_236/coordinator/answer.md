Deprecated both `safe_eval` entry points for 2.21. Calls through `AnsibleModule.safe_eval` delegate to the shared function and emit the same runtime deprecation notice.

`check_type_dict` now tries JSON, then Python literals, then validated `key=value` pairs. It returns only dictionaries and raises descriptive `TypeError`s for malformed input. Added a changelog fragment and regression coverage, including a check that input cannot execute code.

**Validation:** 90 relevant tests passed; `git diff --check` passed. No delegation was used.