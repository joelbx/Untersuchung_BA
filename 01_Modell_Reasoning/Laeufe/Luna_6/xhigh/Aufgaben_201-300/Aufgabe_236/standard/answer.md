Implemented the `safe_eval` deprecation with a runtime 2.21 warning, and changed `check_type_dict` to parse JSON, safe Python literals, or validated key=value pairs without evaluation. Invalid inputs raise descriptive `TypeError`s.

Added changelog entries for both public paths in [deprecate_safe_eval.yml](/app/changelogs/fragments/deprecate_safe_eval.yml).

Verification: 24 existing focused tests passed; `git diff --check` passed.