VERDICT: ACCEPT

The applied patch in [vendors.py](/app/openlibrary/core/vendors.py) meets the language metadata requirements. I found no code defects or test environment problems.

`python -m pytest openlibrary/tests/core/test_vendors.py -q` — 36 passed. `git diff --check` — passed.