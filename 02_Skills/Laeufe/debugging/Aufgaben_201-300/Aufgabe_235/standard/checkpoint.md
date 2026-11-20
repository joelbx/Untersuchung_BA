# Checkpoint

Task: Import alternate-script names linked through MARC 880 for personal authors in 100, 700, and 720.

Status: Investigating existing parser and tests before changes.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find instead.

Root cause: `read_author_person` only sees its source field, and `read_edition` caches only `FIELDS_WANTED`, which excludes 880. Binary `get_linkage` exists but XML has no equivalent. The 700/720 call site does not pass its tag. Existing 245 alternate title parsing demonstrates the linkage format; local fixtures contain 700 `$6=880-04` paired with 880 `$6=700-04/$1`.

Hypothesis: caching 880 and resolving the source field's `$6` against 880 `$6` by tag and occurrence inside `read_author_person` will preserve primary author data and add alternate names across both record types.

Implementation: Added `name_from_list`, cached 880 fields, passed record/tag to personal author parsing, matched `$6` occurrence numbers across 100/700/720 and 880, and deduplicated alternate names. Kept existing Latin initial punctuation behavior while removing terminal punctuation from other names and dates. Organization/event parsing was unchanged. Updated two existing binary fixture expectations and added XML regression coverage.

Verification: Initial regression command `pytest -q openlibrary/catalog/marc/tests/test_parse.py -k 'linked_author_names or linked_contributor_name or name_from_list'` failed during collection because `name_from_list` was missing, as expected. After implementation and fixture updates, `pytest -q openlibrary/catalog/marc/tests` passed (124 tests). `git diff --check` passed. No unresolved check failures.
