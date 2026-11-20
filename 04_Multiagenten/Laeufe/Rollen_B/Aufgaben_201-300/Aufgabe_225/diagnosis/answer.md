The missing data starts in [VulnInfo](/app/models/vulninfos.go:260): it has `AlertDict` but no dedicated `KEVs` field. The new `KEVType`, `KEV`, and source detail structs belong alongside that model; the existing `AlertDict.CISA` field should remain for older JSON.

[FillWithKEVuln](/app/detector/kevuln.go:51) is the main fault. Both its HTTP and database paths retrieve KEV records, then discard their details and create a generic CISA alert. The fix needs to map CISA and VulnCheck entries into `VulnInfo.KEVs`, including dates, XDB records, and reported exploitation. The exact source field names and invalid due date representation remain unverified from repository code alone.

[ScanResult](/app/models/scanresults.go:250) needs `FormatKEVCveSummary()` to count CVEs with at least one KEV. [SortForJSONOutput](/app/models/scanresults.go:388) needs to sort each vulnerability’s KEVs by type, then vulnerability name. Existing tests cover legacy alert sorting, but I found no KEV ingestion or model tests.

I updated [checkpoint.md](/app/.codex-role-output/checkpoint.md). The assigned fault localization role prohibits changing project source or tests, so the requested fix was not applied.