Host blocking now checks the request host and each parent domain against both runtime and config block sets. It checks the per-URL blocking toggle and whitelist first, and treats trailing-dot request hosts like their non-trailing forms. I added the requested `widened_hostnames` helper and tests for its edge cases.

Verification: 426 relevant tests passed, 1 skipped; `git diff --check` passed.