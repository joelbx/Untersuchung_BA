Fixed the admin file upload handler to check that the target folder exists under the configured upload path and is a directory before saving. Invalid targets now return HTTP 500 with `[[error:invalid-path]]`.

Added regression tests for a missing folder and a path that points to a file. The upload test suite passed (43 tests), ESLint passed, and `git diff --check` passed.