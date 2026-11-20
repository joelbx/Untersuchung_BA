The admin file upload endpoint now checks that the target folder exists under the configured upload path before saving. A missing folder returns HTTP 500 with `[[error:invalid-path]]`, and the upload does not create the folder.

Added a regression test. The existing upload suite passed (42 tests), as did ESLint and `git diff --check`.