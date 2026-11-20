# SSH connection issue checkpoint

Status: implementation and focused verification complete.

Changes: SSH plugin resolves runtime command, transfer, retry, timeout, and control path options through `get_option()`. Reset uses the resolved SSH command to check the active master before sending stop. Core duplicate SSH settings removed; play context and smart transport look up plugin settings where needed. CLI-only SSH arguments and private key flow into plugin option resolution. Task executor no longer masks SSH timeout configuration with its default timeout.

TDD: new tests were run red before each implementation step for command options, transfer method, SFTP batch mode, reset check, CLI-only arguments, CLI-only private key, and executor timeout precedence. Existing SSH tests were updated to set plugin options instead of removed core constants.

Verification: `PYTHONPATH=lib:test pytest -q test/units/plugins/connection/test_ssh.py test/units/playbook/test_play_context.py test/units/config/test_manager.py test/units/executor/test_task_executor.py --reruns 0` passed: 102 tests, one existing PyYAML deprecation warning. `git diff --check` passed.

Broad suite: `PYTHONPATH=lib:test pytest -q --reruns 0` was attempted and interrupted at 24% after widespread unrelated collection/fixture failures (102 failed, 510 passed, 14 skipped, 304 errors at interruption). Examples: `test/ansible_test/unit/test_diff.py` could not import `to_text` from installed `ansible_test._internal.util`; `test/ansible_test/validate-modules-unit/test_validate_modules_regex.py` could not import `validate_modules`; collection integration test imports lacked package context. Many `test/units/module_utils/basic/test_argument_spec.py` cases errored. The rest of the broad suite remains unverified because this environment does not run it cleanly with bare pytest.
