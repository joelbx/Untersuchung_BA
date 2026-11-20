Fault-localization progress (2026-10-22):
- `openlibrary/catalog/utils/__init__.py:294` `expand_record` copies `authors` unchanged and never creates `db_name`.
- `openlibrary/catalog/add_book/__init__.py:576-618` `find_enriched_match` calls a local `add_db_name` manually; this helper already handles absent/None authors and name/date formatting.
- `openlibrary/catalog/add_book/match.py:10-17,52-63` duplicates name/date formatting for existing author objects and builds `{name, db_name}` before expansion, omitting date fields from the comparable author.
- `openlibrary/catalog/merge/merge_marc.py:144-149` indexes `i['db_name']` and `j['db_name']`; the level-2 path reaches it when level-1 score is below threshold.
- Reproduced with 1974/1975, matching ISBN, similar author names, threshold 515: `KeyError('db_name')` after expanding both records without manual enrichment.
- Existing focused tests `test_add_db_name` and `TestRecordMatching.test_match_low_threshold` pass (2 passed); they do not cover missing identifiers. The low-threshold fixture supplies `db_name` intentionally different from `name`, so recomputing it changes its score and expected outcome.
- No project source or tests modified. Diagnosis only per specialist assignment.
