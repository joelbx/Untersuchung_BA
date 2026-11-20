Implemented host-scoped monitoring in [utils.py](/app/scripts/monitoring/utils.py) and [monitor.py](/app/scripts/monitoring/monitor.py). The asyncio scheduler gives jobs function-name IDs; the limiter uses `HOSTNAME` to match exact names, prefix wildcards, and short names against fully qualified hosts. The HAProxy job is registered only on `ol-www0`.

Added [haproxy_monitor.py](/app/scripts/monitoring/haproxy_monitor.py) to collect HAProxy CSV metrics and print or send Graphite events. I delegated the scheduler and collector work, integrated both, and completed a read-only review.

Verification: all 19 monitoring tests passed; Ruff and `git diff --check` passed.