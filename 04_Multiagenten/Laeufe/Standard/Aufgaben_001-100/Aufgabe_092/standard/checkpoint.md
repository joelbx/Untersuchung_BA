Task: add Ansible Galaxy collection upgrade support.
Status: implementation complete. Galaxy unit suite passed (181 tests); diff check and compilation passed.
Changes: CLI -U/--upgrade, resolver upgrade handling, installed version idempotency, prerelease filtering, unit and integration coverage.
Integration scenario added in upgrade.yml; requires the existing Pulp/Galaxy integration environment to run.
