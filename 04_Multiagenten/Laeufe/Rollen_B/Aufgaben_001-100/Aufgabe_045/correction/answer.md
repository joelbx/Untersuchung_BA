Updated collection name validation to reject Python keywords and check identifiers with Python’s parser, which is available on supported runtimes. Collection reference validation now applies the same rule to its namespace and collection segments, including Unicode identifiers on Python 3.

Both reviewer test commands pass: **110 passed** and **61 passed**. `git diff --check` also passes.

**TEST_ENVIRONMENT_PROBLEM:** Python 2 is unavailable locally, so compatibility could not be tested on that runtime.