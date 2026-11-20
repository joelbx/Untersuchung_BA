The admin upload endpoint now checks that the requested folder exists as a directory under the configured upload path before saving. Missing paths return HTTP 500 with `[[error:invalid-path]]`.

Added regression tests for a missing folder and a file used as a folder. The upload suite passed (43 tests), and ESLint and `git diff --check` passed.