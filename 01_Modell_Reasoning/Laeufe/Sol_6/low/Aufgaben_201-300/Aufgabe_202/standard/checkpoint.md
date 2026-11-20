Task: validate admin upload target directory using configured upload base; return HTTP 500 [[error:invalid-path]] for missing directory.
Status: implemented in admin upload controller; added regression test. Targeted upload tests: 3 passing. ESLint and git diff --check passed.
