# Checkpoint

Issue: Host blocking must match request hosts and successive parent domains, with whitelist and toggle overrides taking precedence.

Changes:
- Added `urlutils.widened_hostnames`, yielding each hostname and its parents, including the specified edge string behavior.
- Host blocking now exits early when globally/per URL disabled or whitelisted, then checks each widened request hostname against runtime and config block sets. Terminal dots match in either the request or blocklist entry.
- Corrected the per URL toggle test fixture to use an absolute URL; its previous schemeless `QUrl` had an empty host.

Validation: `python -m pytest tests/unit/utils/test_urlutils.py tests/unit/components/test_hostblock.py -q` — 347 passed, 1 skipped.
