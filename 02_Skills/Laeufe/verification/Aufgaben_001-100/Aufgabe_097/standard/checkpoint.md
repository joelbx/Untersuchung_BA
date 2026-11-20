# Checkpoint

Task: update controller Python minimum and collection extraction behavior.

Environment: `rg` unavailable (`/bin/bash: rg: command not found`); using `grep` and `find` locally. No external research or downloads.

Changes: controller minimum set to Python 3.12 in CLI, ansible-test entry point,
ansible-test version list, and package metadata. Both entry points use the same
version error. Collection tar extraction uses `TarFile.getmember(dirname)` with
the incoming value and no private normalized cache. Obsolete controller-only
compatibility branches were removed; remote Python support remains separate.

Verification run on available Python 3.11.13:

- `PYTHONPATH=lib:test/lib python -m pytest -q test/units/cli/galaxy/test_collection_extract_tar.py test/units/utils/collection_loader/test_collection_loader.py`: 73 passed, 1 skipped.
- `PYTHONPATH=lib python bin/ansible --version`: exit 1 with `ERROR: Ansible requires Python 3.12 or newer on the controller. Current version: 3.11.13 ...`.
- `PYTHONPATH=lib:test/lib python bin/ansible-test --version`: exit 1 with the same error.
- `python -m compileall -q lib/ansible/cli/__init__.py lib/ansible/compat/importlib_resources.py lib/ansible/galaxy/collection/__init__.py lib/ansible/galaxy/role.py lib/ansible/utils/collection_loader/_collection_finder.py test/lib/ansible_test/_internal/commands/sanity/validate_modules.py test/lib/ansible_test/_util/target/cli/ansible_test_cli_stub.py test/lib/ansible_test/_util/target/common/constants.py packaging/release.py && git diff --check`: exit 0.
- Final focused pytest rerun after all edits: 73 passed, 1 skipped. Final `compileall` over all changed Python files plus `git diff --check`: exit 0.

Unavailable check: `PYTHONPATH=lib:test/lib python3.12 -m pytest -q test/units/galaxy/test_role_install.py test/units/cli/galaxy/test_collection_extract_tar.py` exited 127 with `/bin/bash: line 1: python3.12: command not found`. Python 3.12 runtime behavior, including role extraction under its tarfile implementation, remains unverified locally. No dependencies downloaded.
