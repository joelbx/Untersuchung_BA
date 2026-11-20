Task: Extract RoleMixin role entry point documentation logic into `_build_doc`.
Status: Implemented `_build_doc` and updated `_create_role_doc` to consume its tuple result. Added unit coverage for names, filtering, full specifications, empty results, and caller behavior.
Verification: `PYTHONPATH=lib python -m pytest test/units/cli/test_doc.py -q` (20 passed); `git diff --check` passed.
