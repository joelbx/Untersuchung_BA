# Checkpoint

Task: Fix host blocking so blocked parent domains cover subdomains, whitelist rules override blocking first, URL inputs and trailing-dot hostnames are handled, and preserve the specified hostname widening edge cases.

Implemented:
- Added `urlutils.widened_hostnames`, yielding the original hostname and successive left-stripped parents while preserving edge-form string behavior.
- Host blocking now checks the global/per-URL toggle, short-circuits whitelist matches, and tests each widened hostname against runtime and config block sets, including trailing-dot equivalents.
- Preserved existing empty-host exact-match behavior for hostless QUrls.

Verification: `pytest -q tests/unit/utils/test_urlutils.py tests/unit/components/test_hostblock.py` — 347 passed, 1 skipped.
