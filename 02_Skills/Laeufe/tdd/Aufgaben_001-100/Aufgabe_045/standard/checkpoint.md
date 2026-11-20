# Checkpoint

Task: reject Python keywords and invalid identifiers in collection FQCNs; remove duplicate legacy validation from Galaxy dependency resolution.

Changes: added `is_python_identifier` in `_collection_finder.py`; `AnsibleCollectionRef.is_valid_collection_name` now checks exactly two identifier segments and returns a boolean. Galaxy requirement classification calls that method. Removed `_is_py_id`, `_is_fqcn`, and their Python 2 fallback from `dataclasses.py`. Added parameterized regression cases in `test_collection_loader.py`.

Verification:
- RED: `PYTHONPATH=lib:test python -m pytest -q test/units/utils/collection_loader/test_collection_loader.py -k test_collection_name_requires_python_identifiers` failed on seven expected invalid names; two valid cases passed.
- GREEN: same command with `--reruns 0` passed (9 cases).
- `PYTHONPATH=lib:test python -m pytest -q test/units/utils/collection_loader/test_collection_loader.py test/units/galaxy/test_collection.py test/units/galaxy/test_collection_install.py --reruns 0`: 108 passed, 8 failed, 23 errors. Galaxy failures include `NotImplementedError: an AnsibleCollectionFinder has not been installed in this process`; local pytest invocation lacks the repository test harness setup. Thus Galaxy suite success is unverified.
- `timeout 60s env PYTHONPATH=lib:test python -m pytest -q --reruns 0 > /tmp/collection-validation-pytest.log 2>&1`: exit 124 at 56%, with many failures/errors already shown, including `test/units/cli/test_console.py`, `test/units/cli/test_galaxy.py`, and `test/units/module_utils/basic/test_argument_spec.py`. Full suite result remains uncertain due to timeout and harness requirements.
- `git diff --check` passed.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
- Final focused file run: `PYTHONPATH=lib:test python -m pytest -q test/units/utils/collection_loader/test_collection_loader.py --reruns 0`: 66 passed, 1 external PyYAML deprecation warning.
