# Coverstore archival checkpoint

Implemented ten-digit cover ID helpers, deterministic item/batch paths and URLs, uncompressed zip staging, upload existence checks, four-size batch finalization, batch file locking, database status fields and indexes, and record-driven remote retrieval. Legacy tar reading remains supported. Added focused archival tests and updated coverstore documentation.

Verification: `ruff check` on changed Python modules passed; `python -m pytest openlibrary/coverstore/tests -q` passed (21 passed, 7 skipped).
