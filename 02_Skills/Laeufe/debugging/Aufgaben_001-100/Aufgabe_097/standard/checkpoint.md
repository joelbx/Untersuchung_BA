# Checkpoint

Task: raise the controller Python minimum and update related collection handling and release notes.

Status: investigation started. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep` and `find` instead. No code changes yet.

Root cause: controller minimum is duplicated in CLI, package metadata, and ansible-test constants. Collection extraction still uses `_ansible_normalized_cache`, a workaround for Python issue 47231, and strips a trailing separator before lookup. The explicit task requirement sets the new minimum at 3.12.

Baseline reproduction: `PYTHONPATH=lib:test/lib pytest -q test/units/cli/galaxy/test_collection_extract_tar.py` exited 1: three tests failed with `TypeError: 'Mock' object is not subscriptable` at the private-cache lookup, as expected for the new getmember contract.

Environment: only Python 3.11 is installed (`python --version` => 3.11.13; no python3.12 executable found). Post-change runtime tests will require a narrow test harness workaround for the controller import gate; that does not certify execution on Python 3.12.

Implementation: enforce Python >=3.12 in both controller entry points and package metadata; restrict ansible-test controller version list to 3.12/3.13; remove the TarFile private cache and use getmember(dirname) unchanged; simplify obsolete controller compatibility paths and constraints; add a major-change fragment. The collection loader retains its remote-Python import fallback because it is also used on supported remote interpreters.

Verification:
- `PYTHONPATH=lib python -c 'import ansible.cli'` exited 1 with `ERROR: Ansible requires Python 3.12 or newer on the controller. Current version: 3.11.13 ...` (expected rejection).
- `python bin/ansible-test --version` exited 1 with the identical rejection message (expected).
- `PYTHONPATH=lib:test/lib python -c 'import sys; original = sys.version_info; sys.version_info = (3, 12, 0, "final", 0); import ansible.cli; sys.version_info = original; import pytest; raise SystemExit(pytest.main(["-q", "test/units/cli/galaxy/test_collection_extract_tar.py", "test/units/galaxy/test_collection_install.py", "test/units/utils/collection_loader/test_collection_loader.py", "test/units/galaxy/test_role_install.py", "test/units/cli/test_cli.py"]))'` exited 0: 159 passed, 1 skipped. This bypasses the import gate only; it does not test a real Python 3.12 runtime.
- `python -m compileall -q lib/ansible/cli lib/ansible/compat/importlib_resources.py lib/ansible/galaxy lib/ansible/utils/collection_loader/_collection_finder.py lib/ansible/template/native_helpers.py packaging/release.py test/lib/ansible_test/_internal/commands/sanity/validate_modules.py test/lib/ansible_test/_util/target/cli/ansible_test_cli_stub.py && git diff --check` exited 0.

Uncertainty: no Python 3.12 interpreter is installed, so Python 3.12 runtime behavior remains unverified locally. No dependencies were downloaded.
