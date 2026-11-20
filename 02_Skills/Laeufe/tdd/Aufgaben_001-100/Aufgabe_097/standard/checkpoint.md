# Progress checkpoint

Task: raise the controller Python minimum and simplify collection compatibility code.

Status: implementation complete in checked-out files. Controller minimum is 3.12 in CLI, ansible-test, and package metadata; 3.10/3.11 remain managed-node versions. Collection tar extraction uses exact `TarFile.getmember(dirname)` lookup without `_ansible_normalized_cache`. Older controller-only compatibility paths and comments were simplified, and a breaking-change fragment was added.

Verification:
- `PYTHONPATH=lib:test/units pytest -q --override-ini=addopts='' test/units/test_python_support_constants.py test/units/template/test_template_utilities.py test/units/cli/galaxy/test_collection_extract_tar.py test/units/cli/test_python_version.py`: 15 passed.
- `PYTHONPATH=lib:test/units pytest -q --override-ini=addopts='' test/units/cli/galaxy/test_collection_extract_tar.py` failed before the collection fix because `_extract_tar_dir` used `_ansible_normalized_cache`; passed after the fix.
- `PYTHONPATH=lib:test/units pytest -q --override-ini=addopts='' test/units/cli/test_python_version.py` failed before the version gate change because Python 3.11 was accepted; passed after the change.
- `PYTHONPATH=lib:test/units pytest -q --override-ini=addopts='' test/units/test_python_support_constants.py` failed before moving 3.10/3.11 to `REMOTE_ONLY_PYTHON_VERSIONS`; passed after.
- `PYTHONPATH=lib:test/units timeout 30s pytest -q --override-ini=addopts=''`: exit 3 during integration test collection; `test/integration/targets/async/library/async_test.py` runs `AnsibleModule` at import and exits because pytest stdin is not valid module JSON.
- `PYTHONPATH=lib:test/units timeout 30s pytest -q --override-ini=addopts='' test/units`: exit 3 during collection; `test/units/cli/arguments/test_optparse_helpers.py` imports `ansible.cli`, which correctly exits under installed Python 3.11.13 with the new Python 3.12 minimum.

Uncertainty: no Python 3.12 interpreter is installed, so the full controller suite and the removed 3.11 compatibility branches could not be exercised on a supported interpreter. No dependencies were downloaded.
