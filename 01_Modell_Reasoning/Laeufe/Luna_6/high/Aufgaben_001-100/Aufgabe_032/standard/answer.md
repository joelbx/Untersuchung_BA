Updated [async_wrapper.py](/app/lib/ansible/modules/async_wrapper.py) with centralized JSON termination and atomic job-file writes. Completion, setup, fork, and timeout records now include consistent lifecycle fields and the job ID; timeout records include the child PID.

Verification passed: `pytest -q test/units/modules/test_async_wrapper.py` (1 test) and `git diff --check`.