# Checkpoint

Task: Resolve inconsistent output, error handling, and job result writes in `lib/ansible/modules/async_wrapper.py`.

Plan: Inspect the wrapper and local async-related tests; implement centralized JSON termination and atomic job writes while preserving existing behavior; run relevant existing tests.
