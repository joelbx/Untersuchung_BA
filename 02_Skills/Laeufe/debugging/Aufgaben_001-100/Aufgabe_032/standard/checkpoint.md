# Async wrapper checkpoint

Status: Root cause identified; preparing failing tests.

Evidence: `daemonize_self` uses `sys.exit` with text on fork failures; `_run_module` writes successful module JSON without lifecycle fields or job ID; timeout supervisor exits without final job record; main setup and catch paths print different JSON shapes. `_run_module` opens `.tmp` before running and only renames at end, so stale `.tmp` can remain on interrupted execution. Existing unit coverage checks only rc and stderr. `async_status` expects `started`/`finished` and adds missing values as a compatibility fallback.

Hypothesis: centralizing termination and job writes, then making the supervisor own timeout records, will make each path consistently structured while preserving the existing immediate response contract.

Check limitation: Running `PYTHONPATH=lib python lib/ansible/modules/async_wrapper.py ...` failed before `main()` because Python loads `lib/ansible/modules/tempfile.py` in place of the standard library `tempfile` module (`ImportError: cannot import name 'mkstemp' from partially initialized module 'tempfile'`). The wrapper is normally copied to a remote temporary path; run the end-to-end check from a copied path to avoid this repository layout collision.

Resolved: Added `end` and atomic `jwrite`; all job results now carry the same ID and lifecycle fields. First fork failure writes a failed job record and one JSON response. Setup and argument errors use structured responses. Daemon or supervisor errors write failed records. Timeout now uses a real deadline, kills and reaps the child, then writes a failed record with its PID. Cleanup follows `preserve_tmp` in supervisor completion and child error paths.

Verification: `python -m pytest -q -o addopts='' test/units/modules/test_async_wrapper.py` passed (8 tests). `git diff --check` and `python -m compileall -q lib/ansible/modules/async_wrapper.py` passed. A copied-wrapper process check passed for normal completion and one-second timeout; the corresponding timeout case is now a persistent unit test. The in-place direct execution check remains invalid due to the repository's `tempfile.py` import collision, not a wrapper behavior failure.

Constraints: Local repository only; preserve git history, index, and harness configuration. Run relevant existing tests.
