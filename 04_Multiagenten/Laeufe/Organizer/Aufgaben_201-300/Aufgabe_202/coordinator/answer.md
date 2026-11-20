The admin file upload endpoint now checks that the requested folder is a directory under the configured upload path before saving. A missing folder returns HTTP 500 with `[[error:invalid-path]]`. I added a regression test for that case.

The admin upload suite passed (17 tests), as did ESLint and `git diff --check`. I made the changes directly; no delegation was used.