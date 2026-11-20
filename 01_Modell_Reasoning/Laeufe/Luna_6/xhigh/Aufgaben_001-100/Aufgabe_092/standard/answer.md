Implemented `--upgrade` / `-U` for collection installs and passed it through the CLI to the installer. Upgrade mode resolves requested collections to the newest permitted version, keeps compatible installed dependencies, updates incompatible dependencies when dependency resolution is enabled, and skips reinstalling when the selected version is already installed. `--no-deps` leaves dependencies untouched, and prerelease selection is covered in both upgrade and regular resolution.

Added CLI and resolver unit coverage, plus [upgrade.yml](/app/test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml) for upgrade scenarios.

Validation: **147 unit tests passed**; `git diff --check` and integration YAML parsing passed. The integration tasks were not run against Galaxy/Pulp services.