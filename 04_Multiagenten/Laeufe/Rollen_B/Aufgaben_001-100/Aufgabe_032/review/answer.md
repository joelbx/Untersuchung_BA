VERDICT: FIX

**Code defect:** The early usage error omits `ansible_job_id` even when a job ID was supplied. `PYTHONPATH=lib python -m ansible.modules.async_wrapper reviewjob 10` exited with JSON containing no job identifier. Derive the ID before this exit and include it in the response. Directory creation errors also omit the cleanup policy reported by the successful immediate response; include it once determined. See [async_wrapper.py](/app/lib/ansible/modules/async_wrapper.py:211).

**Tests:** `PYTHONPATH=lib python -m pytest -q test/units/modules/test_async_wrapper.py` — 4 passed. The passing tests do not cover the early usage response.

**TEST_ENVIRONMENT_PROBLEM:** None.