# Checkpoint

Task: implement `ansible-galaxy collection install --upgrade` with dependency upgrade handling, constraint safety, opt-in prereleases, requirements-file parity, and idempotency.

Scope: inspect and edit checked-out repository code and tests only. Preserve git history, index baseline, and harness configuration.

Progress: implemented the collection-only `--upgrade`/`-U` option and resolver behavior; added focused CLI/resolver unit coverage plus `test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml` for direct, requirements-file, dependency, no-deps, prerelease, and repeat-upgrade cases. Validation passed: 147 relevant unit tests, `git diff --check`, and YAML parsing of the integration task files.
