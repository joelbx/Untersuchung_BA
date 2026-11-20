The admin file upload endpoint now checks that the requested folder exists under the configured upload path before saving. Missing folders and paths that name a file return HTTP 500 with `[[error:invalid-path]]`.

The admin upload suite passed (18 tests). ESLint and `git diff --check` passed.