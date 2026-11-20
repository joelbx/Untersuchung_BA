# Checkpoint

Task: implement alternate-script author-name parsing in `openlibrary/catalog/marc/parse.py`.

Completed:
- Added public `name_from_list(name_parts: list[str])` normalization.
- Resolved 100, 700, and 720 `$6` links against corresponding 880 fields and deduplicated alternate names.
- Preserved primary person fields, normalized `$a` and `$d` values, and left 110/111 handling unchanged.
- Updated existing binary MARC output snapshots for normalized author names and newly parsed alternate names.

Verification:
- `python -m pytest openlibrary/catalog/marc/tests/test_parse.py -q`: 59 passed.
- `git diff --check`: passed.
