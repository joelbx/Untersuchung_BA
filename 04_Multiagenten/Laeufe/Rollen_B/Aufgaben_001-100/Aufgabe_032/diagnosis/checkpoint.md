# async_wrapper fault localization

Inspected `lib/ansible/modules/async_wrapper.py`, `lib/ansible/modules/async_status.py`, action plugin call site, and existing async tests. Existing unit test passes (1 test); it only checks a successful module result and stderr.

Likely faults in `async_wrapper.py`: `daemonize_self` uses string `sys.exit` on both fork errors; `_run_module` drops job ID/lifecycle fields on success, opens a second `.tmp` outside its try block, and has no final record on timeout; `main` setup/fatal errors omit job ID and lifecycle fields. Timeout supervisor exits after killing child without writing a failed result. `_make_temp_dir` treats any EEXIST as success, even an existing regular file. Action plugin consumes `_ansible_suppress_tmpdir_delete` from the immediate response. `async_status` infers `finished=1` only when `started` is absent, so explicit final flags are needed if completed records retain `started`.

Specialist scope: diagnosis only; no project source or test edits.
