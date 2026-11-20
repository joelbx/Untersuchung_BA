# Checkpoint

Task: resolve inconsistent async_wrapper output and job record behavior.

Implementation in `lib/ansible/modules/async_wrapper.py`:
- Added `end(res, exit_msg)` for a single flushed JSON response followed by process termination.
- Added `jwrite(info)` for atomic job file replacement via `<job_path>.tmp`, with I/O failures logged and re-raised.
- Standardized immediate, setup, fork, and fatal error responses; result records include lifecycle fields and the same async job ID.
- Added timeout result records with the supervised child PID, timeout diagnostics, and cleanup policy.
- Kept errors from the forked worker out of the launcher's stdout stream while retaining them in the job record.

Verification: `pytest -q test/units/modules/test_async_wrapper.py` passed (1 test); `git diff --check` passed.
