The admin file upload endpoint now checks that the requested folder exists under the configured upload path before saving. Missing folders and paths to files return HTTP 500 with `[[error:invalid-path]]`.

Added regression tests in [test/uploads.js](/app/test/uploads.js:403). The admin upload suite passed (18 tests), and ESLint passed.