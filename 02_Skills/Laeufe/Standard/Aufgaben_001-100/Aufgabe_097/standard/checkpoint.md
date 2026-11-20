# Checkpoint

Task: raise the controller Python minimum to 3.12 and update collection tar extraction behavior.

Implemented: controller entry-point checks and packaging metadata, ansible-test controller version list, tar directory lookup through `getmember`, removal of the private TarFile cache, related controller compatibility cleanup, unit test updates, and changelog fragment.

Checks:
- `PYTHONPATH=lib:test/lib pytest -q test/units/cli/galaxy/test_collection_extract_tar.py test/units/utils/collection_loader/test_collection_loader.py`: 73 passed, 1 skipped on Python 3.11.13.
- `python -m py_compile lib/ansible/cli/__init__.py lib/ansible/compat/importlib_resources.py lib/ansible/galaxy/collection/__init__.py lib/ansible/galaxy/role.py lib/ansible/utils/collection_loader/_collection_finder.py packaging/release.py test/lib/ansible_test/_internal/commands/sanity/validate_modules.py test/lib/ansible_test/_util/target/cli/ansible_test_cli_stub.py`: passed.
- `git diff --check`: passed.
- `PYTHONPATH=lib:test/lib python bin/ansible-test --version`: exits 1 with `ERROR: Ansible requires Python 3.12 or newer on the controller. Current version: 3.11.13 ...`; expected on this interpreter.
- `PYTHONPATH=lib:test/lib pytest -q test/units/galaxy/test_collection_install.py test/units/galaxy/test_collection.py test/units/galaxy/test_role_install.py test/units/cli/galaxy/test_collection_extract_tar.py`: exits 3 during collection with `SystemExit: ERROR: Ansible requires Python 3.12 or newer on the controller. Current version: 3.11.13 ...` from `lib/ansible/cli/__init__.py`.
- `PYTHONPATH=lib:test/lib pytest -q test/units/galaxy/test_role_install.py test/units/galaxy/test_collection.py`: same exit 3 during collection.

Uncertainty: Python 3.12+ is not installed in this workspace. The full Galaxy installation tests and runtime behavior of the new 3.12 tarfile path cannot be verified here. No dependencies were downloaded.

Final review: added the Python 3.13 package classifier, clarified the remote Python tarfile fallback comment, and reran `git diff --check` successfully. No `_ansible_normalized_cache` references remain in the collection installer or its focused test.
