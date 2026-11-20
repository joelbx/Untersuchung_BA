VERDICT: ACCEPT

The applied patch meets the requested behavior. The import API forwards `override-validation=true` through `load()` to `validate_record`; the default validation checks remain in place, and `is_promise_item` handles case-insensitive `promise:` prefixes. I found no code defect or TEST_ENVIRONMENT_PROBLEM.

`python -m pytest -q openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/tests/catalog/test_utils.py` — **117 passed**. `git diff --check` also passed. No project code was changed during review.