VERDICT: FIX

The applied patch still drops valid seeds when a POST body contains both a valid indexed field and a malformed index. For example, `seeds--0--key=/books/OL1M&seeds--oops--key=bad` produces `seeds=[]`. In [lists.py](/app/openlibrary/plugins/openlibrary/lists.py:71), the resulting mapping is treated as one invalid seed. Preserve valid numeric entries and ignore malformed ones.

`python -m pytest openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/tests/test_utils.py -q` completed: **17 passed, 1 warning**. The failing case was reproduced separately. TEST_ENVIRONMENT_PROBLEM: none. No project code was changed during this independent review.