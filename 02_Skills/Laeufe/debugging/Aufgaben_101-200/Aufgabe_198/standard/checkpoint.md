# Checkpoint

Task: Resolve Red Hat OVAL advisory and fix-state handling, remove Red Hat Gost CVE path.

Status: Investigating repository and reproducing failures before changes. `rg` is unavailable (`/bin/sh: rg: not found`); using local `find` and `grep`.

Root cause: `convertToDistroAdvisory` always returns an advisory; `AppendIfMissing` dereferences it. `isOvalDefAffected` returns immediately on `NotFixedYet` without using resolution metadata, and HTTP/DB collection plus `toPackStatuses` drop fix state. `NewGostClient` still selects RedHat. Pinned goval-dictionary revision lacks `AffectedResolution`; locally cached v0.9.5 contains it.

Pattern and hypothesis: The existing OVAL matcher already filters by Amazon repository, architecture, modularity, enabled modules, and installed version. Keep those checks and resolve a matching `AffectedResolution` only for `NotFixedYet` packages. Hypothesis is that changing the dependency and propagating a state from a matching resolution component fixes missing statuses; filtering advisory IDs by family fixes invalid advisories. `GOPROXY=off go test ./oval -run '^TestConvertToDistroAdvisoryPrefixes$' -count=1` fails as expected for RHEA on Red Hat and RHSA on Oracle. Baseline selected tests `GOPROXY=off go test ./oval ./gost -run 'TestPackNamesOfUpdate|TestSetPackageStates' -count=1` pass.

Implementation: Updated cached goval-dictionary dependency to v0.9.5; limited advisories to matching family prefixes; carried fix state through the OVAL matcher, HTTP/DB collection, package status conversion and Red Hat update; prevented Gost from detecting Red Hat family CVEs. Added regression cases for valid/invalid advisory IDs, resolution states, module streams, status preservation and Gost selection.

Additional failing regressions observed before their fixes: `GOPROXY=off go test ./oval -run '^TestUnfixedResolution/other_module_stream$' -count=1` selected a `Will not fix` state from another module stream; `GOPROXY=off go test ./oval -run '^TestRedHatUpdatePreservesFixState$' -count=1` lost a previously known state when a later definition had no state. Both now pass.

Final verification: `GOPROXY=off go test ./oval ./gost ./detector -count=1` passed for all three packages; `git diff --check` passed. No offline tooling prevented verification.
