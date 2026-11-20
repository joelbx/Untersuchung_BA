# WinRM kinit debugging checkpoint

Status: investigating root cause. Repository baseline: a77dbf0. `rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

Required behavior: configurable kinit arguments, deterministic command construction across subprocess and pexpect, one invocation and unique credential cache per authentication attempt.

## Investigation and hypothesis

Existing WinRM code builds `[self._kinit_cmd] + delegation_flags + [principal]`; the configured `kinit_cmd` is therefore passed as a single executable token. The reported path-with-arguments failure follows from this construction. Current tests pass (26/26), and there is no `kinit_args` option. The closest working pattern is the existing explicit `kerberos_command` option plus a shared command list used by both subprocess and pexpect. Hypothesis: a dedicated string option, parsed into tokens before the shared list is passed to either runner, will support custom flags and supersede the delegation default. Existing `NamedTemporaryFile` creation already occurs once per `_kerb_auth` call and passes its name through `KRB5CCNAME` to both runners.

A minimal pre-fix test for multiple arguments and delegation precedence was added to both runner cases. Command: `python -m pytest -q test/units/plugins/connection/test_winrm.py -k 'kinit_success'`. Result: 4 expected failures (custom args omitted; `-f` still appended), 6 passes, exit 1.

Implementation check: first full WinRM run had 33 passes and one failure in the newly added cache test. The test indexed `call_args_list` using the `mock_calls` tuple layout; production behavior was not implicated. Correcting the test's call extraction before rerunning.

## Final implementation and verification

Added documented `kinit_args` connection option exposed through `ansible_winrm_kinit_args`. When provided, `shlex.split` supplies all command arguments and suppresses the default delegation `-f`; without it, delegation still adds `-f`. Both runners consume the same assembled command list; pexpect now slices that list without mutating it. Existing per-attempt `NamedTemporaryFile` behavior was retained and covered with a new two-attempt test for each runner.

Final check: `python -m pytest -q test/units/plugins/connection/test_winrm.py` exited 0 (34 passed). `git diff --check` exited 0. A Windows host integration test was not run because no target host is available in the local repository environment; subprocess and pexpect behavior were verified by local unit tests.
