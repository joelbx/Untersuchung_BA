Task: Fix atomic_move default file permissions and missing-mode warnings in module_utils/basic and common/file.
Status: Complete. Changed _DEFAULT_PERM to 0600; atomic_move uses the existing DEFAULT_PERM & ~umask chmod and tracks new destinations for modules with an omitted mode; _return_formatted emits exact per-path warnings; set_mode_if_different removes handled paths.
Validation: PYTHONPATH=lib python -m pytest -q --reruns 0 --forked test/units/module_utils/basic (299 passed, 14 skipped). git diff --check passed.
Constraints observed: Local repository and existing tests only; git history, index, and harness configuration untouched.
