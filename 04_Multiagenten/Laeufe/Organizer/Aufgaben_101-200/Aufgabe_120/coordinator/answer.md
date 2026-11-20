Implemented zip based cover archival with zero padded item, batch, and filename paths. Covers keep their local database paths while staged; finalization verifies that all four zips are uploaded and contain the expected images before setting remote URLs and `uploaded=true`. Batch locks prevent overlapping local archival runs. I also removed the hardcoded tar redirect, added the status columns and indexes, and documented the layout.

Existing tar rows are **not automatically repackaged**. If a batch contains one, finalization stops rather than assigning it a URL for an image absent from the zip.

The coverstore suite passed: **20 passed, 7 skipped**. No delegation was used.