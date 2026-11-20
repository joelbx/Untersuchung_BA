# Checkpoint

Task: fix process-to-package association with multiple installed RPM versions or architectures.
Status: investigating root cause before edits.
Constraint: local repository evidence and tests only; no downloads.
Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local alternatives.

Root cause: RPM ownership lookup returns name/version/release, but `Packages` is keyed by name and can retain only one installed version or architecture. `yumPs` uses `FindByFQPN`, so an owner from another installed variant cannot be found. Debian and Red Hat also duplicate process collection.
Hypothesis: using ownership package names as map keys eliminates variant mismatch; parsing RPM diagnostic lines separately preserves valid partial results and rejects unexpected output.
Reproduction: `GOPROXY=off GOSUMDB=off go test ./scan -run '^TestParseOwnerPkgs$' -count=1` failed as expected with `o.parseOwnerPkgs undefined` (exit 1). The compiler also emitted a warning from sqlite3-binding.c.

Implementation: `pkgPs` collects executable and mapped paths and associates processes by package name; Debian and Red Hat post-scan paths use it. `getOwnerPkgs` parses RPM output, ignores three known path diagnostics, deduplicates names, and errors on malformed output or execution failure.
Verification: `GOPROXY=off GOSUMDB=off go test ./scan -count=1 && git diff --check` passed (exit 0). The existing sqlite3-binding.c compiler warning still appears.
