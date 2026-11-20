Task: implement host-scoped scheduling for monitoring jobs and the requested HAProxy monitor interfaces.
Status: implemented asyncio scheduler, environment-based host gating, HAProxy collector, Docker service IP lookup, and async monitor entrypoint. Monitoring tests pass (8 tests); Ruff passes. Final diff check pending.
Constraints observed: local code and tests only; git history, index baseline, and harness configuration untouched.
