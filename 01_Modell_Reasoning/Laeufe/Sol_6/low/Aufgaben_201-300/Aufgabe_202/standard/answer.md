The admin upload endpoint now checks that the requested folder exists under the configured upload path and is a directory before saving a file. A missing folder returns HTTP 500 with `[[error:invalid-path]]`.

I added a regression test. The three relevant upload tests pass, and ESLint passes for the changed files.