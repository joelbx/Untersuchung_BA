# Progress

- Added `-U`/`--upgrade` to collection install and passed it through the installer and resolver.
- Resolver now selects the newest permitted direct requests, preserves compatible installed dependencies, replaces incompatible dependencies during upgrades, and excludes prereleases unless requested.
- Added unit coverage and `tasks/upgrade.yml` integration scenarios, including requirements files and idempotency.
- Final local Galaxy and CLI unit suite: 267 passed with `ANSIBLE_DEVEL_WARNING=False`; integration and changelog YAML parsed; `git diff --check` passed.
- Integration tasks require the repository's Galaxy/Pulp test services and were not executed locally.
