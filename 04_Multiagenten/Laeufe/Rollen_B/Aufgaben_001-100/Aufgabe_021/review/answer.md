VERDICT: FIX

[List.get_book_keys()](/app/openlibrary/core/lists/model.py:153) resolves every seed’s document before filtering for books. A subject lookup failure can therefore stop list search even when the list contains a valid edition. In a local reproduction with one subject and one edition, a mocked subject lookup raised `RuntimeError: subject lookup unavailable`. Filter seed keys before resolving documents, so book key collection does not fetch subject metadata.

`python -m pytest -q openlibrary/tests/core/lists/test_model.py openlibrary/plugins/openlibrary/tests/test_lists.py` — **12 passed**. No project code was changed during this review.