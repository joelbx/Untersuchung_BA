Updated hosts blocking to check the request host and each parent domain against both blocked sets. The blocking toggle and URL whitelist take precedence, and matching handles trailing dots. Added `urlutils.widened_hostnames` and tests for these cases.

Verification: the focused suite reported **357 passed, 1 skipped**; `git diff --check` passed.