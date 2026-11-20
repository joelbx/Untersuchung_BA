Host blocking now checks the request host and each parent domain against both block sets. It applies the enabled setting and whitelist override first, and treats trailing dots equivalently. I added `widened_hostnames` and regression tests for those cases.

Verification: 357 relevant tests passed, 1 skipped; the updated per-URL toggle test also passed.