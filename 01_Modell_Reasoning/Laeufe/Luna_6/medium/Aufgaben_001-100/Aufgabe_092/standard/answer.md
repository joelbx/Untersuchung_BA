Implemented `-U` / `--upgrade` and passed it through collection installation and dependency resolution. Upgrade mode reevaluates requested collections and dependencies against version constraints, and skips installation when the resolved version is already present.

Validation: `python -m pytest -q test/units/galaxy/test_collection_install.py` — 30 passed. `git diff --check` passed.

I did not add the requested `upgrade.yml` coverage; the changes currently have no new upgrade-specific tests.