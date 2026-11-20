Updated host blocking so a blocked domain also blocks its subdomains. The blocker checks the per-URL toggle and whitelist first, then checks each parent hostname against both block sets. Trailing dots are normalized for matching, and `urlutils.widened_hostnames` provides the requested hostname sequence.

Relevant tests passed: **357 passed, 1 skipped**.