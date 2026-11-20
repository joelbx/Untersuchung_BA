Implemented the tombstone notice as a semantic paragraph and updated the reply preview to identify the person being replied to, with an accessible cancel control.

Added reusable [CancelButton](/app/src/components/views/buttons/Cancel.tsx) with configurable sizing, and updated the reply preview styles to use it.

Verification passed: the focused `MessageComposer` test, TypeScript check, and `git diff --check`.