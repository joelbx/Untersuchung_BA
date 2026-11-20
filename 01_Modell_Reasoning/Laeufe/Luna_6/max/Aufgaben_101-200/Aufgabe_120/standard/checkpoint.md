# Coverstore archival issue checkpoint

- Implemented `Cover`, `Batch`, `CoverDB`, `ZipManager`, and `Uploader` in `openlibrary/coverstore/archive.py`.
- Switched batch packaging to uncompressed, deduplicated zip files with the documented 10/4/2 digit identifier layout; added batch locks, exact upload checks, retry-safe finalization, and URL-based DB references.
- Added local zip-member reading and URL redirects, `failed`/`uploaded` schema defaults and indexes, explicit new-cover defaults, and updated archival documentation.
- Verification: `python -m compileall -q openlibrary/coverstore`; `pytest -q openlibrary/coverstore/tests` (18 passed, 7 skipped).
- Constraints followed: repository code/tests only; no downloads, delegation, history edits, index baseline changes, or harness configuration changes.
