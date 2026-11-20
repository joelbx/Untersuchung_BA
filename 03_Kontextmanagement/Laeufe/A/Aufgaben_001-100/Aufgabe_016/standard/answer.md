Implemented host-scoped scheduling in the checked-out repository. [OlAsyncIOScheduler](/app/scripts/monitoring/utils.py) reads `HOSTNAME` from the environment, supports exact names, trailing prefix wildcards, and short names for fully qualified hosts, and gives jobs their function name as the default ID. Disallowed jobs are skipped during registration.

Added the async [monitoring entrypoint](/app/scripts/monitoring/monitor.py) and [HAProxy collector](/app/scripts/monitoring/haproxy_monitor.py), including Graphite event serialization. The HAProxy job is scoped to `ol-www0`.

Verification: all 9 monitoring tests passed; `git diff --check` passed.