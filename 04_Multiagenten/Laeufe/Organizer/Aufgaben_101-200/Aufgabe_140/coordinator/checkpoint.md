# Checkpoint

Task: Fix hosts-based blocking so parent domains cover subdomains, with whitelist and enabled checks taking precedence. Add `widened_hostnames` to `qutebrowser/utils/urlutils.py` with specified string semantics.

Status: Implemented directly without delegation. HostBlocker checks the enabled setting, then whitelist, then each hostname and parent against both runtime and config block sets. Request hosts and blocklist entries with trailing dots match their ordinary forms. Added focused tests for the utility, subdomains, full URLs, whitelisting, and trailing dots. Corrected an existing per-URL toggle test to use a URL with a parsed host.

Verification: `pytest -q tests/unit/components/test_hostblock.py tests/unit/utils/test_urlutils.py tests/unit/config/test_configutils.py` passed: 437 passed, 1 skipped. `git diff --check` passed before final comment-only adjustment.
