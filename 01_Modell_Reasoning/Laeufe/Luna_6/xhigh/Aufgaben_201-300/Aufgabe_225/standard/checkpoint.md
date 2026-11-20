# Checkpoint

Task: add first-class KEV data to the vulnerability model, support CISA and VulnCheck data and legacy alerts, and implement KEV summary and deterministic JSON ordering.

Implemented:
- Added `KEV`, `KEVType`, CISA/VulnCheck detail structs, and `VulnInfo.KEVs`.
- Added `ScanResult.FormatKEVCveSummary` and included the count in the text report header.
- Sorted KEVs by source and vulnerability name, and sorted VulnCheck detail slices.
- Updated `FillWithKEVuln` to convert CISA catalog records into first-class KEVs while keeping the legacy CISA alert; its decoder handles source-tagged VulnCheck records and their XDB/reported exploitation details when present in the payload.
- Invalid or placeholder due dates become `nil`.

Validation: `go test ./models ./detector` passed.
