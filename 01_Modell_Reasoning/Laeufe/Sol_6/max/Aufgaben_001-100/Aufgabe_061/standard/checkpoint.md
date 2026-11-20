# Checkpoint

- Task: fix package ownership lookup for installed packages with multiple architectures or versions.
- Findings: Debian and Red Hat duplicate process collection. Red Hat matches RPM ownership by FQPN even though installed packages are keyed by name and only one entry per name is retained.
- Plan: centralize process collection in `base.pkgPs`, use distribution ownership lookups, and parse RPM ownership output with explicit ignored diagnostics and malformed-line errors.
- Implemented: shared `base.pkgPs`, Debian and Red Hat ownership callbacks, RPM line parsing with explicit ignorable diagnostics, and name-based lookup for `needsRestarting`.
- Added focused tests for mixed RPM versions/architectures, malformed and ignorable output, process association deduplication, and path quoting.
- Verification: `GOPROXY=off GOSUMDB=off go test ./scan ./models` passed; `git diff --check` passed.
- Remaining model constraint: the installed package inventory is keyed by package name, so it retains one version/architecture per name. This change associates processes to that inventory entry by ownership name and removes FQPN mismatch warnings; it does not add separate inventory entries for every installed variant.
- Status: implementation and review complete.
