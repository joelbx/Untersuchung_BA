# Fault localization progress

Inspected controller entry points, package metadata, collection tar extraction, compatibility branches, and existing unit tests. No project source or tests changed.

- `lib/ansible/cli/__init__.py:14` accepts Python 3.10+; `setup.cfg:30,40` advertises/requires 3.10+; `test/lib/ansible_test/_util/target/common/constants.py:12` lists 3.10 and 3.11 as controller versions; `bin/ansible-test:25` derives its distinct user-facing error from that list. Explicit requirement says controller floor 3.12, although issue title only says to drop 3.10.
- `lib/ansible/galaxy/collection/__init__.py:1605-1610` creates `_ansible_normalized_cache` for each TarFile. `_extract_tar_dir` at 1690 strips trailing separator and indexes that cache; direct `tar.getmember(dirname)` is required, preserving the incoming name and mapping missing member to the specified AnsibleError.
- Existing `test/units/cli/galaxy/test_collection_extract_tar.py` injects the private cache and expects legacy behavior; it would need adjustment to exercise `getmember` and exact error text in a repair. No tests run because this role permits diagnosis only.
- `lib/ansible/utils/collection_loader/_collection_finder.py:35-39` already imports `reload as reload_module` inside a Python 2 fallback; `string_types` checks there are likely the requested `str` simplification. Other old-version branches include `lib/ansible/compat/importlib_resources.py` and `lib/ansible/galaxy/role.py`; remote-node compatibility should be treated separately from controller floor.
- `test/lib/ansible_test/_data/requirements/constraints.txt:4-5` has a pre-3.11 dependency split; `changelogs/fragments/` contains no visible fragment announcing dropped controller Python support.
