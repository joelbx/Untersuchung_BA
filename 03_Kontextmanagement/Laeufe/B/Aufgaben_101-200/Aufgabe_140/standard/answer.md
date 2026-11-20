Updated host blocking to check each parent hostname in both blocked sets, with an early whitelist override and trailing-dot normalization. Added `urlutils.widened_hostnames` and regression tests.

Validation passed: 419 relevant tests passed, one skipped; `git diff --check` was clean.