Updated notifications to render string HTML through sanitization, make links open in a new tab with `rel="noopener noreferrer"`, and deduplicate non-success messages by explicit key, string text, or notification ID. Repeated success messages remain visible. React element content is still supported.

Verification passed: 8 focused tests, the components TypeScript check, and `git diff --check`.