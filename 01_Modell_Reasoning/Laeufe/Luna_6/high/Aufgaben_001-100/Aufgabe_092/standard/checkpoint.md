# Checkpoint

Task: implement `ansible-galaxy collection install --upgrade` (`-U`) with constraint-aware, idempotent dependency upgrades and opt-in prerelease handling.

Implemented:
- Added the collection install CLI option and passed its default-false value into `install_collections`.
- Upgrade resolution reevaluates explicitly requested collections, prefers newest compatible versions for those roots, and preserves installed transitive dependencies when they still satisfy constraints. A selected version already installed is skipped.
- Resolver carries upgrade intent and continues applying version constraints. `--no-deps` still disables dependency traversal. The existing explicit prerelease pin behavior remains, while `--pre` allows prereleases for floating/range selection.
- Added integration coverage in `test/integration/targets/ansible-galaxy-collection/tasks/upgrade.yml` for stable upgrades, idempotency, prereleases, and requirements files; included it from the integration target main task.

Verification:
- `ANSIBLE_DEVEL_WARNING=False python -m pytest -q test/units/galaxy/test_collection_install.py test/units/cli/test_galaxy.py` — 140 passed.
- `python -m compileall -q ...` — passed.
- `git diff --check` — passed.
- The integration play was authored but not run; this checkout's integration target requires Galaxy/Pulp services.
