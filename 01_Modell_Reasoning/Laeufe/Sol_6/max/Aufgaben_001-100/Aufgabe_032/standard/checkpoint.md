# async_wrapper checkpoint

- Goal: make every async wrapper exit path emit consistent JSON and write job state atomically.
- Repository state: clean at start; target is `lib/ansible/modules/async_wrapper.py` and its existing unit tests.
- Implemented centralized `end` and atomic `jwrite`, consistent job IDs and lifecycle fields, structured setup/fork/timeout errors, and watcher cleanup.
- Added unit coverage for atomic replacement and real forked runs (success, timeout, preservation, fork failures, missing/invalid arguments, directory errors, and invalid module output).
- Final verification: `python -m pytest -q test/units/modules/test_async_wrapper.py` passed (14 tests); `py_compile` and `git diff --check` passed.
