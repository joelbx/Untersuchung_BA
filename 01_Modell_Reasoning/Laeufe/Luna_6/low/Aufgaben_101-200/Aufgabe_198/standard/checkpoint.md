# Checkpoint

Completed the Red Hat OVAL fix-state and advisory changes. Supported advisory prefixes are now filtered by distro, fix states flow through OVAL package status collection, and Red Hat-family Gost CVE detection routes to the no-op client so OVAL owns detection. Red Hat Gost API enrichment helpers remain available. `isOvalDefAffected` now returns `(affected, notFixedYet, fixState, fixedIn, err)` and retains repository, architecture, modularity, kernel, and version checks.

The pinned goval-dictionary normalized model omits `AffectedResolution` (although a newer code path in its Red Hat ingest contains the field); a compatibility extraction reads that member when it exists in normalized definition JSON, leaving an empty state otherwise.

Verification: `go test ./...` passed. `git diff --check` passed. Existing OVAL tests were updated only for the helper's added return value.
