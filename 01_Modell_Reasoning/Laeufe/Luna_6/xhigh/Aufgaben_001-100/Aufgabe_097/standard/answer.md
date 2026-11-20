Implemented the Python 3.12 controller minimum across the CLI, ansible-test, packaging metadata, and changelog. Python 3.10 and 3.11 remain in ansible-test’s remote-only matrix.

Collection extraction now passes `dirname` unchanged to `tar.getmember()`, raises the required error when the member is missing, and no longer uses `_ansible_normalized_cache`. I also removed controller compatibility workarounds that are obsolete at the new minimum.

**Validation:** 239 relevant unit tests passed. Both CLI entry points produced the same rejection message under Python 3.11; the test suite used a temporary shim to bypass only the new startup gate because this workspace has no Python 3.12 interpreter. `git diff --check` passed.