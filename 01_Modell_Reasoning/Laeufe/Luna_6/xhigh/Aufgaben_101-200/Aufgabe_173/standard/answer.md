Implemented HA database candidate selection: the proxy now shuffles matching services, retries tunnel connectivity failures, and reports an error if no candidate is reachable. Authorization retains all candidates, and tests can control ordering and simulate per-server tunnel outages.

Also added host IDs to server strings, stable name/host sorting, and name deduplication for `tsh db ls`.

Existing tests passed: `api/types`, `lib/reversetunnel`, `lib/srv/db`, and `tool/tsh`.