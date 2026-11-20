# Checkpoint

Task: Fix notification HTML rendering, link safety, and deduplication.
Status: Complete.

Changes:
- Sanitize string notification HTML with DOMPurify and render supported markup.
- Set secure navigation attributes on notification links, including React element links.
- Derive deduplication keys from an explicit key, string text, or notification id; exempt success notifications.
- Add focused notification rendering and manager tests.

Verification:
- Focused Jest tests: 10 passed.
- Components TypeScript check: passed.
- Prettier check and git diff check: passed.
