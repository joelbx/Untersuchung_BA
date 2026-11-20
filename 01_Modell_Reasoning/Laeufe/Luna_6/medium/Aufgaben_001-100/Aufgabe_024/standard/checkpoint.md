# Checkpoint

Implemented in `openlibrary/catalog/add_book/load_book.py`:
- Honorific removal now accepts and returns a name string, ignores case for supported leading titles, protects the configured exception names despite punctuation/case, and leaves honorific-only names intact.
- `build_query` applies honorific removal to each copied author name before matching/import.
- Author name query asterisks are escaped. Surname matching runs only when both birth and death years can be extracted, uses the surname token, and queries date fields by year patterns.

Validation: ran `python -m pytest openlibrary/catalog/add_book/tests/test_load_book.py -q`. 17 passed and 11 failed. Ten failures are legacy tests calling the now-required string API with `author=` dictionaries. The remaining failure expects `*` to act as a wildcard in a regular name query, contrary to the issue requirement to escape it. `git diff --check` passed.
