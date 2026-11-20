# Checkpoint

Task: Deprecate both safe_eval entry points and make check_type_dict deterministic.
Status: Implementation, changelog, and regression tests complete.
Changes: check_type_dict uses JSON, then ast.literal_eval, then strict key=value parsing; safe_eval emits an Ansible deprecation for 2.21; the wrapper delegates to it.
Verification: 95 validation/parameters tests and 23 safe_eval tests pass; git diff --check passes. A broader combined basic suite has unrelated global-warning state failures, while representative failures pass in isolation.
