Implemented the Python 3.12 controller minimum across the CLI, `ansible-test`, package metadata, controller version matrix, and controller-only test dependency markers. Added a changelog fragment documenting the removal of Python 3.10 and 3.11 support.

Collection directory extraction now passes `dirname` unchanged to `tar.getmember()`, raises the required `AnsibleError` when missing, and no longer uses `_ansible_normalized_cache`. Simplified the import compatibility code and added the `reload_module` import.

**Verification:** the collection extraction tests passed (3 tests), and `git diff --check` passed. Broader tests could not collect because this workspace runs Python 3.11.13, below the new minimum.