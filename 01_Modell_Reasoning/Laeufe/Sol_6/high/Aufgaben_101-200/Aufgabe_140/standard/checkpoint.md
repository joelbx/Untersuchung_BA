# Checkpoint

- Goal: make hosts-based blocking cover parent domains and preserve whitelist/toggle overrides.
- Initial state: working tree clean; relevant code is in `qutebrowser/components/hostblock.py` and `qutebrowser/utils/urlutils.py`.
- Implemented `urlutils.widened_hostnames`, parent-domain checks after the toggle and whitelist overrides, and trailing-dot normalization for loaded hosts.
- Added tests for widening edge cases, runtime and config block sets, full request URLs, whitelist overrides, trailing dots, and disabled blocking.
- Verification: URL utility and host blocker tests passed (368 passed, 1 skipped, 1 deselected before the last test addition); focused host blocker rerun passed (49 passed, 1 skipped, 1 deselected).
