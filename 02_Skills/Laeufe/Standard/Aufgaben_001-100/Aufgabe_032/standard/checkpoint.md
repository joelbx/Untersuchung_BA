# async_wrapper repair checkpoint

- Updated `lib/ansible/modules/async_wrapper.py` with `end` for single JSON stdout responses and `jwrite` for atomic job-file replacement.
- Added consistent job IDs, lifecycle fields, structured failure records, timeout PID/context, and cleanup policy in the immediate response. Child startup errors are reported to the launcher through the pipe.
- Added unit tests for `end`, atomic `jwrite`, and initial fork failure.
- `python -m pytest test/units/modules/test_async_wrapper.py -q`: 4 passed.
- `python -m py_compile lib/ansible/modules/async_wrapper.py` and `git diff --check`: passed.
- Manual `python -m ansible.modules.async_wrapper` subprocess checks passed for valid JSON success, module exception, timeout, directory creation failure, and invalid time limit. The success, exception, and timeout checks also read final job records and verified the same job ID; timeout included `child_pid`.
- Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches used `find` and `grep`. Direct script invocation (`python lib/ansible/modules/async_wrapper.py`) fails because `lib/ansible/modules/tempfile.py` shadows the standard library `tempfile` module while `multiprocessing` imports. Module invocation (`python -m ansible.modules.async_wrapper`) allowed end-to-end checks. This pre-existing direct invocation limitation was not changed.
