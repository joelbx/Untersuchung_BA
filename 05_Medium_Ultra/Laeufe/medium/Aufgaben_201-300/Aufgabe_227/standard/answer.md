The MIME suffix workaround now checks only runtime Qt for its 6.2.3 and 6.7.0 bounds. I clarified the `compiled` parameter, changed the `compiled=True, exact=True` error to `RuntimeError`, and added tests with differing runtime, compiled Qt, and PyQt versions.

All 31 relevant tests passed; `git diff --check` found no formatting issues.