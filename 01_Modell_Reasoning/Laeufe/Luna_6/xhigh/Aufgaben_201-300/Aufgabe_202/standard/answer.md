Updated [admin/uploads.js](/app/src/controllers/admin/uploads.js:201) to validate that the requested folder exists as a directory under the configured upload path before saving. Invalid paths return `[[error:invalid-path]]` with HTTP 500, and the temporary upload is cleaned up.

Verification: ESLint passed, and the admin upload test group passed (16 tests) using a temporary local Redis service.