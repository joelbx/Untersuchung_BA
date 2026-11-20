# Checkpoint

Implemented collection install upgrade plumbing (`-U`/`--upgrade`) through the CLI, installer, resolver builder, and dependency provider. Upgrade mode reevaluates installed requirements and avoids preferring installed candidates, while normal installs preserve current preference behavior. Resolved versions already installed are skipped in upgrade mode, preserving idempotency.

Validation: `python -m pytest -q test/units/galaxy/test_collection_install.py` — 30 passed. `git diff --check` passed.
