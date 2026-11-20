# Checkpoint

Task: deprecate `safe_eval` entry points and make `check_type_dict` deterministic and non-evaluating.

Status: completed repository edits. `safe_eval` records an Ansible deprecation for version 2.21, and the `AnsibleModule` wrapper delegates to it. `check_type_dict` tries JSON, then Python literals, then validated key=value pairs. Added changelog fragment and focused tests.

Verification: 107 relevant validation and safe_eval tests pass; `git diff --check` passes. A broader run including `test_argument_spec.py` had two failures caused by process-wide warnings left by earlier cases; each failed case passes in isolation.
