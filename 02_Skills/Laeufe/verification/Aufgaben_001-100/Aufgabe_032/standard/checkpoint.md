# Checkpoint

Task: make async_wrapper JSON responses, job records, timeout handling, and cleanup consistent.

Implemented centralized `end` and atomic `jwrite`; running and completed records share the job ID and lifecycle fields. Startup, fork, directory, timeout, and module failures use structured results. Timeout records include `child_pid`. Temporary module cleanup follows `preserve_tmp` in completion and failure paths.

Verification run:
- `python -m pytest test/units/modules/test_async_wrapper.py -q`: 4 passed.
- `git diff --check && python -m py_compile lib/ansible/modules/async_wrapper.py && git status --short`: exit 0.
- Direct early-error probes using `PYTHONPATH=lib python -m ansible.modules.async_wrapper ...` emitted one JSON object and exited 1.

Tooling notes: `rg` is unavailable (`/bin/bash: line 1: rg: command not found`), so repository searches used `find` and `grep`. Direct script probe `PYTHONPATH=lib python lib/ansible/modules/async_wrapper.py` failed because local `lib/ansible/modules/tempfile.py` shadowed the standard-library `tempfile` module (`ImportError: cannot import name 'mkstemp' from partially initialized module 'tempfile'`). Probes using `python -m ansible.modules.async_wrapper` avoided that repository invocation issue.
