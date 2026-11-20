The admin file upload endpoint now checks that the requested folder exists as a directory under the configured upload path before saving. Invalid targets return HTTP 500 with `[[error:invalid-path]]`.

Added regression tests for missing folders and file targets in [test/uploads.js](/app/test/uploads.js). The admin upload tests, ESLint, and `git diff --check` passed.