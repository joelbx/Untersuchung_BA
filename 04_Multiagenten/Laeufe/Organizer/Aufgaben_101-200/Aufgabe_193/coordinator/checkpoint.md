# Checkpoint

Task: unify ansible-galaxy requirements installation for roles and collections.
Status: implementation complete; tests passed.
Changes: implicit install processes both types at default paths; explicit type or custom role path skips other type with diagnostic; empty input skips; parser context initialized; dependency queue force behavior adjusted.
Verification: 113 CLI galaxy tests and 19 cli/galaxy tests passed with PYTHONPATH=lib:test and ANSIBLE_DEVEL_WARNING=False; py_compile and git diff --check passed.
Delegation: none.
