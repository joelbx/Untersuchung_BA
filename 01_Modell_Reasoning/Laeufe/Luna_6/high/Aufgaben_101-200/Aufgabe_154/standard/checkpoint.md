# Checkpoint

Task: Fix Windows stderr handling for embedded CLIXML in the SSH connection plugin.

Plan:
- Inspect the current CLIXML parser and its existing tests.
- Add a byte-preserving stderr scanner with UTF-8/cp437 decoding and failure-safe replacement.
- Update the Windows `exec_command` path and regex handling.
- Run the focused existing tests.
