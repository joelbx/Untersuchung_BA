# Checkpoint

Task: resolve flexible Ansible collection manifest configuration in `/app`.

Initial findings: repository is clean; `rg` is unavailable, so use `find` and `grep`. Likely implementation and unit coverage are under `lib/ansible/galaxy/collection` and `test/units/galaxy`.

Next: inspect `_build_files_manifest`, its callers, and existing tests; implement sentinel and symlink behavior as required; run focused existing tests.

Implementation complete:
- Missing `manifest` metadata is now represented by `ansible.utils.sentinel.Sentinel`.
- `_build_files_manifest` treats `Sentinel`, `{}`, and `None` as no active manifest control, preserving the walk-based format 1 manifest and `build_ignore` handling.
- The walk skips symlinks resolving outside the collection for both files and directories; internal links retain the existing single linked-path entry behavior.

Verification: `python -m pytest -q test/units/galaxy/test_collection.py` passed (62 tests). `git diff --check` passed.
