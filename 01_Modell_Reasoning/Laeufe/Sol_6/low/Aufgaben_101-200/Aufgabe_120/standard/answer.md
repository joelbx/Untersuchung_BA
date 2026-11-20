Implemented zip based cover staging, zero-padded item and batch paths, per-batch locking, upload verification, and database finalization. Retrieval now uses archive.org URLs for covers marked `uploaded`. The schema and README reflect the new flow.

Relevant coverstore tests passed: **13 passed, 7 skipped**. The skipped browser tests did not exercise the new flow.