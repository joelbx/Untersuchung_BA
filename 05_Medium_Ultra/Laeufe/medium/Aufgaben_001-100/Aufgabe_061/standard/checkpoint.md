# Checkpoint

Task: Fix process-to-package ownership mapping for installed package variants in Debian and Red Hat scanners.

Current state: Shared `base.pkgPs` collects process files and listening ports, then attaches each process by package name. Debian and Red Hat `postScan` call it with their ownership lookups. RPM ownership parsing skips expected file errors, deduplicates names, and errors on malformed output. Added `TestParseOwnerPkgs`. Full `scan` package tests pass with `GOPROXY=off`; `git diff --check` passes.
