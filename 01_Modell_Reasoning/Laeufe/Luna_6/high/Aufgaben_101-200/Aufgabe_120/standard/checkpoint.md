# Coverstore archival issue checkpoint

- Implemented `Cover`, `CoverDB`, `ZipManager`, `Uploader`, and `Batch` in `openlibrary/coverstore/archive.py`.
- Archival now stages uncompressed, deduplicated zip batches with zero-padded member names and per-zip process locks. Batch processing uploads and verifies all four variants before updating DB URLs/status.
- Added `failed` and `uploaded` columns/indexes in both schema definitions; cover retrieval now reads canonical Archive.org URLs.
- Documented the item/batch naming and current zip workflow in the coverstore README.
- Verification: focused coverstore suite passed (18 passed, 7 skipped); `compileall` and `git diff --check` passed; direct smoke check confirmed naming, zip layout, and deduplication.
- Constraints followed: no network research/downloads, no delegation, no git history/index baseline/harness changes.
