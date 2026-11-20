Implemented `ansible-galaxy collection install --upgrade` (`-U`) and passed the option through installation and dependency resolution. Upgrades honor version constraints, update required dependencies while preserving compatible ones, and skip reinstalling collections already at the selected version. Prereleases require `--pre`.

Added integration coverage in [upgrade.yml](/app/test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml), CLI and resolver unit coverage, documentation, and a changelog fragment.

**Verification:** 144 relevant unit tests passed; changed YAML files parsed successfully and `git diff --check` passed. The integration task wasn’t run because it requires Galaxy/Pulp services.