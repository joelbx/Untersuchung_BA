Updated the coverstore archival flow to stage uncompressed ZIP batches, use zero-padded IDs and paths, verify all four uploads before finalization, and write archive.org URLs to completed cover records. Per-batch locks prevent overlapping runs. The schema now includes `failed` and `uploaded` flags, and retrieval uses stored URLs while retaining access to legacy tar records.

**Verification:** 22 coverstore tests passed, 7 were skipped; lint and diff checks passed.

Existing remote tar batches still need their source images to be repackaged as ZIPs. Finalization rejects a ZIP that lacks eligible covers.