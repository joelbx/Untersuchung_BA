Fixed `List.get_book_keys()` to filter for book and work keys before resolving documents, so an unavailable subject lookup cannot interrupt book key collection. Added a regression test for a list containing both a subject and a valid edition.

The reviewer’s exact test command passed: **13 tests passed**.