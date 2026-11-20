Task: add an ICX logging module with ICX-specific command syntax and idempotent state handling.
Status: implemented icx_logging with aggregate normalization, running-config parsing,
ICX command generation, validation, check mode, and focused unit tests.
Verification: 99 ICX unit tests passed; py_compile and git diff --check passed.
Constraints: local repository and existing tests only; preserve git history, index, and harness configuration.
