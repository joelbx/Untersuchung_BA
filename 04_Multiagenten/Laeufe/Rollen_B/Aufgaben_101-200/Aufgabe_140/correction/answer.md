Fixed the trailing-dot mismatch by normalizing hostnames as blocklist entries are loaded. Added regression tests for saved and config blocklists, including parent domains and dotted request hosts.

The reviewer’s exact test command passes: **358 passed, 1 skipped**.