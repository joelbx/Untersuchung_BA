# Checkpoint

Implemented `urlutils.widened_hostnames` and parent-domain matching in hosts-based blocking, with enabled and whitelist checks ahead of matching. Added tests for widening edge forms, runtime and config blocks, trailing-dot requests, whitelist overrides, and per-URL disabling. Relevant unit suites: 426 passed, 1 skipped, 8 benchmark cases deselected. `git diff --check` passed.
