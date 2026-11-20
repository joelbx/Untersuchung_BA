Updated [async_wrapper.py](/app/lib/ansible/modules/async_wrapper.py) to use consistent JSON exit responses, atomically replace job files, and include job IDs, lifecycle fields, and timeout diagnostics in result records. Added focused tests in [test_async_wrapper.py](/app/test/units/modules/test_async_wrapper.py).

Verification passed: 5 unit tests, a local timeout run, and `git diff --check`.