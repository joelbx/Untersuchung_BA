Implemented `ansible-galaxy collection install -U/--upgrade`. It selects the latest version within the stated constraints, updates incompatible dependencies, honors `--pre` and `--no-deps`, applies to requirements files, and skips versions already installed.

Added [upgrade.yml](/app/test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml). All 148 relevant local unit tests pass, and the task YAML parses. The integration tasks require a Galaxy/Pulp service and were not run.

This work item is complete.