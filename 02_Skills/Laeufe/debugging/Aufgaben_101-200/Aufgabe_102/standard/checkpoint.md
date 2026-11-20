# Checkpoint

Task: add Linux locally reachable IP range facts from scope-host routes.
Status: investigating existing collector, schema, and tests before edits.
Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.

Investigation: `LinuxNetwork.populate` reads only `ip addr` per interface and default route probes. Those do not represent arbitrary host-scope local route prefixes. `NetworkCollector._fact_ids` controls subset selection; a Linux-only fact ID can be added on `LinuxNetworkCollector`. No existing Linux network unit tests. `ip` binary is absent in this container, so command behavior will be verified with recorded-style mocked output. Hypothesis: querying `ip -4/-6 route show table local scope host` and parsing `local` route destinations yields the missing ranges, independent of interface names.

Implemented: `LinuxNetwork.get_locally_reachable_ips(ip_path)` queries IPv4 and IPv6 local routing tables with host scope, accepts local route destinations, canonicalizes with `ipaddress`, de-duplicates and sorts by numeric address/prefix. `populate` exposes `locally_reachable_ips`; the Linux collector registers the fact ID. Missing `ip` and failed family queries return empty lists with warnings.

Reproduction: `python -m pytest -q test/units/module_utils/facts/network/test_linux.py` failed before fix with 4 expected failures (missing method/fact). Verification: `python -m pytest -q test/units/module_utils/facts/network` passed, 9 tests. `git diff --check` passed. Runtime query against the host could not be checked because `command -v ip` returned no path; route parsing is verified through mocked command output.
Final verification after formatting: `python -m pytest -q test/units/module_utils/facts/network && git diff --check` exited 0; 9 tests passed.
