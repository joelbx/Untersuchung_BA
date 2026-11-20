# Checkpoint: author matching issue

- Located matching and import logic in `openlibrary/catalog/add_book/load_book.py`; dates in `openlibrary/catalog/utils/__init__.py` already have a year-based helper, but comparison needs consistent extracted years.
- `remove_author_honorifics` currently mutates/returns a dictionary and handles only simplistic prefix cases.
- Matching currently allows wildcard names directly and tries surname lookup even without valid dates.
- Next: adjust helper API and callers, harden exact/alternate/surname matching, and run relevant existing catalog tests.
