Task: Fix hosts-based blocking so parent domains cover subdomains, with whitelist and toggle precedence.
Status: implemented and verified.
Changes: added urlutils.widened_hostnames; host blocker checks whitelist early, then request host and successive parents in both block sets, treating trailing-dot forms equivalently. Added helper and blocker regression tests; repaired the per-URL toggle test to use an actual URL and explicitly enable global blocking.
Verification: full hostblock, urlutils, and configutils suite passed (425 passed, 1 skipped) before final trailing-dot block-entry addition; focused follow-up passed (13 passed); full hostblock suite passed (38 passed, 1 skipped).
Constraints followed: local code/tests only; git history, index, and harness configuration untouched.
