# Checkpoint

Task: implement Trivy OS release metadata, artifact naming, package CVE detection gating, and ScannedBy reuse.

Phase 1 underway. Initial source inspection shows parser currently stores `trivy-target` in Optional and uses result Target as ServerName; detector/util.go identifies Trivy through Optional. No edits to implementation yet.

Phase 1: Trivy report OS metadata carries Name, but parser ignores it. Parser uses per-result Target for ServerName and Optional for identity. Detector reuse reads Optional. DetectPkgCves currently gates only on Release and package count; adding Release would run OVAL/GOST on Trivy results. Last commit is a lint fix; working tree began clean.

Phase 2: ScanResult already has Release and ScannedBy fields. Existing parser fixtures contain OS Name and artifact names. Existing detector path already logs skip reasons but lacks a centralized gate.

Phase 3 hypothesis: copying OS.Name and ArtifactName into ScanResult and using ScannedBy for identity will supply metadata without Optional; a gate excluding Trivy and unsupported/missing metadata will prevent duplicate package detection. Focused tests added and first offline run in progress.

Phase 4: First offline test run failed in TestSetScanResultMeta for all four metadata cases (expected name/release/Optional mismatches). Updated parser to use ArtifactName, append :latest for untagged container images, store OS.Name in Release, and clear Optional. Detection now uses ScannedBy and a single eligibility gate; OVAL/GOST errors are logged and returned. Updated existing parser fixtures.

Verification: `GOPROXY=off go test ./contrib/trivy/parser/v2 ./detector -count=1` exited 0. `GOPROXY=off go test ./contrib/trivy/... ./detector -count=1` exited 0. `git diff --check` exited 0. No offline tooling blockers.
