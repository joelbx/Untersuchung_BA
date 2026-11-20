Implemented the zip based archival flow in [archive.py](/app/openlibrary/coverstore/archive.py): padded ID and URL helpers, batch paths, deduplicated uncompressed zips, per batch locking, upload verification, and DB finalization to archive.org URLs.

Updated cover serving to read pending local zip members or redirect to stored remote URLs. Added the `failed` and `uploaded` columns and indexes, initialized those fields for new covers, and documented the ID and path schema in the README.

Verification passed: `python -m compileall -q openlibrary/coverstore`, `git diff --check`, and the coverstore suite (**18 passed, 7 skipped**).