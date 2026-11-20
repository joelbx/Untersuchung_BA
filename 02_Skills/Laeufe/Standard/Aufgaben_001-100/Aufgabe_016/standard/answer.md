Implemented host-scoped monitoring registration using `OlAsyncIOScheduler`. Jobs keep function-name IDs, and `limit_server` checks `HOSTNAME` against exact names and trailing prefix wildcards, including short names for fully qualified hosts. Added the HAProxy CSV monitor and Graphite event interfaces.

Verification: all 9 monitoring tests pass, Ruff lint passes, and `git diff --check` passes.