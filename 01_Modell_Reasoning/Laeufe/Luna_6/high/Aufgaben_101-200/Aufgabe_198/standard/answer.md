Implemented family-specific advisory filtering, OVAL fix-state propagation, and removed Red Hat CVE detection through gost. Updated existing OVAL assertions.

Verification: `go test ./...` passes; `git diff --check` passes.

One limitation: this checkout’s pinned goval-dictionary model has no `AffectedResolution` field. The code reads that field when available, but this dependency cannot provide the resolution value. The dependency upgrade needed to fully populate those states remains unresolved.