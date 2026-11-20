The admin file upload endpoint now checks that the target is an existing directory under the configured upload path before saving. Missing directories and file paths return HTTP 500 with `[[error:invalid-path]]`.

Added integration tests for both cases. The full upload test file passed: 43 tests.