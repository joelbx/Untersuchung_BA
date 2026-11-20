Task: Fix notifications with HTML content and duplicate messages.
Status: Complete.
Changes: String content is sanitized with DOMPurify and rendered as HTML. All notification anchors, including React element content, receive rel="noopener noreferrer" and target="_blank". Explicit keys are honored; otherwise string text or the id supplies the key. Non-success notifications deduplicate by key; success notifications can repeat.
Verification: Focused notification Jest suite passed (6 tests); components TypeScript check passed; ESLint on changed files passed; git diff --check passed.
