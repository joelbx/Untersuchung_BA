The [admin upload handler](/app/src/controllers/admin/uploads.js:190) now checks that the target is an existing directory under the configured upload path before saving. Invalid targets return HTTP 500 with `[[error:invalid-path]]`. [Regression tests](/app/test/uploads.js:392) cover missing folders and paths that point to files.

Verification: all 43 upload tests passed, and ESLint passed.