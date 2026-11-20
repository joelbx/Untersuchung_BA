# Checkpoint

Task: repair Red Hat family OVAL advisory filtering, fix-state propagation, and remove Gost RedHat CVE path.
Status: complete.
Changes: use cached goval-dictionary v0.9.5 with AffectedResolution; filter advisory identifiers by family; propagate fix states and fixed versions; remove Gost RedHat DetectCVEs selection and method; add OVAL regression tests.
Verification: GOPROXY=off go test -mod=mod ./oval ./gost ./detector ./server ./scanner (all passed); git diff --check (passed).
