# Checkpoint

Completed the Dialog abstraction and migrated ModalTwo to it. Dialog forwards dialog attributes, children, and ref to a native `<dialog>` when supported, and uses an accessible `div` host when dialog modal operations are unavailable. ModalTwo renders the host open and marks it modal.

Verification: targeted ModalTwo and Dialog suites passed (11 tests); Dialog suite passed again after the final prop-forwarding adjustment (2 tests); components TypeScript check passed; Prettier check and git diff --check passed.
