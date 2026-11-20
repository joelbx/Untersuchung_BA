Task: Fix ModalTwo JSDOM dialog compatibility.
Status: Complete. Added a public forwardRef Dialog component that uses native dialog when supported and an accessible div host otherwise; ModalTwo uses it with open and aria-modal. Added tests for role queries, operability, host refs, attributes, and native/fallback hosts.
Verification: Focused Jest suites passed (11 tests); package TypeScript check, Prettier check, and git diff --check passed.
Constraints: Checked-out files only; no git history, index baseline, or harness configuration changes.
