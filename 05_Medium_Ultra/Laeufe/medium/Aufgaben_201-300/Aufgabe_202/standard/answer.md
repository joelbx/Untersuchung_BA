The admin file upload endpoint now checks that the requested folder is a directory under the configured upload path before saving. Missing folders and paths that point to files return HTTP 500 with `[[error:invalid-path]]`.

Added request tests for both cases. The four focused upload tests pass, and ESLint and `git diff --check` pass.