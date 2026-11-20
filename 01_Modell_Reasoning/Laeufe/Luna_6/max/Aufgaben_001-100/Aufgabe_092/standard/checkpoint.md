# Upgrade collections implementation checkpoint

- Objective: add `ansible-galaxy collection install --upgrade` (`-U`) with constraint-aware upgrades, transitive dependency handling, opt-in prereleases, requirements-file support, and idempotency.
- Repository: `/app`; initial worktree was clean. No `AGENTS.md` files were found.
- Changes completed:
  - Added the collection install CLI flag and passed it through `install_collections`, `_resolve_depenency_map`, and `build_collection_dependency_resolver`.
  - Upgrade mode resolves requested collections against available versions; matching installed versions are skipped without reinstalling.
  - Compatible installed dependencies remain preferred; incompatible installed dependencies are upgraded only with `--upgrade`. Without upgrade, conflicts fail without changing installed dependencies. `--no-deps` avoids dependency changes.
  - Prereleases are filtered unless `--pre` is set, for both install and download resolution. Updated examples/tests accordingly.
  - Added `test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml`, dependency fixtures, CLI/provider unit coverage, docs, and a changelog fragment.
- Verification: `./bin/ansible-test units test/units/galaxy/test_collection_install.py test/units/cli/test_galaxy.py` passed (144 tests). `git diff --check` and YAML parsing passed. The integration task file was not executed because this target needs configured Galaxy/Pulp services.
- Final review: changed files are limited to the CLI, resolver/install code, relevant docs/changelog, and Galaxy tests/fixtures. No integration services were available for executing the new integration task.
