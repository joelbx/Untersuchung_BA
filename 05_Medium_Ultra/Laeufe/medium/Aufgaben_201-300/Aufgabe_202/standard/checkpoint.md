Task: Validate that admin file upload target directories exist beneath the configured upload path.

Status: Implemented admin upload folder validation against the configured upload path. Missing folders, paths outside the upload directory, and file targets return [[error:invalid-path]] through the existing HTTP 500 handler.

Verification: Focused upload controller tests passed (4 passing). ESLint and git diff --check passed.
