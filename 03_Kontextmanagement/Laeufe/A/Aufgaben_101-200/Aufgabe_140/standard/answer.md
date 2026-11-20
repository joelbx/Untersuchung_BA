Fixed hosts-based blocking. It now checks the request host and each parent domain against both block sets, treats trailing dots equivalently, and applies whitelist overrides before host matching. Added `widened_hostnames` and tests for the specified edge cases.

Verification: 374 tests passed, 1 skipped; `git diff --check` passed.