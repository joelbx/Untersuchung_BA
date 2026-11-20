Fault localization complete. No project source or tests changed.
- archive.py: TarManager writes tar/index; archive() selects only archived=false and id>7999999, writes per-cover tar references and deletes local images before upload confirmation; no locking or retry-safe dedupe. is_uploaded() checks legacy tar/index via shell grep.
- code.py: cover.GET hard-codes 8000000 <= id < 8810000 to tar redirects, independent of DB status; fallback reads tar offsets. This explains stale links for the specified range.
- schema.py/schema.sql: cover has archived only; failed/uploaded columns and indexes absent.
- coverlib.py: find_image_path/read_file support local files and tar offsets, not zip member or remote-state semantics.
- Existing tests test_code.py and test_coverstore.py assert legacy tar/index behavior; test_webapp.py archival test is DB-dependent and skipped at class scope.
- Required fix behavior: strict 10/4/2 digit mapping; uncompressed zip per size and 10k batch; verify all expected remote zip files before marking an entire non-failed batch uploaded and changing all filename variants; idempotent retries and non-overlapping batch claims; retrieval follows completed DB state, preserving legacy coverage where needed.
