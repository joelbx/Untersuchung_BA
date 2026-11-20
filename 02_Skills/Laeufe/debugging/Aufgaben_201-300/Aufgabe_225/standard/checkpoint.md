# Checkpoint

Task: add first-class KEV data to vulnerability model and populate it from CISA and VulnCheck.
Status: investigating existing model, source types, and tests.

Investigation: VulnInfo only has AlertDict; detector/kevuln.go discards go-kev response details and sets a generic CISA alert. Local go-kev db.Response has CISA []KEVuln and VulnCheck []VulnCheck; DB interface exposes GetKEVByCveID. Root cause: detector has no model mapping for either source. Hypothesis: a shared response-to-KEV mapper used by HTTP and DB paths will preserve source metadata and let summaries/sorting use the dedicated field.

New evidence: detector regression check failed because go.mod pins go-kev v0.1.4-0.20240318121733-b3386e67d3fb, whose DB interface has only legacy CISA lookup and no VulnCheck types. A newer v0.1.4-0.20240830055848-169d68089b5c module is already cached locally and has the needed combined Response. Hypothesis updated: select cached newer go-kev module to support both sources.

Implementation: added models.KEV and source-specific structs; VulnInfo.KEVs; KEV CVE summary and deterministic sorting. Detector maps both CISA and VulnCheck response records in HTTP and DB paths. Updated go-kev to the locally cached release that supports both sources; no network download.
Verification: initial models regression failed for missing KEVs/types as expected. Initial detector test failed because pinned go-kev lacked Response, VulnCheck types, and GetKEVByCveID. After dependency update, `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test -mod=readonly ./models ./detector -count=1` passed. `git diff --check` passed. No remaining offline tooling uncertainty.
