Updated [async_wrapper.py](/app/lib/ansible/modules/async_wrapper.py) to use centralized JSON termination and atomic job-file writes. Job records now carry a consistent job ID and lifecycle fields; timeout records include the child PID, and setup and fork failures produce structured errors.

The existing async wrapper unit test passes, and the module compiles.