Host blocking now checks the request host and each parent domain against both block sets. Whitelist matches take precedence, trailing-dot hosts are normalized for matching, and the new `widened_hostnames` utility covers the specified edge cases.

Relevant tests passed: **356 passed, 1 skipped**.