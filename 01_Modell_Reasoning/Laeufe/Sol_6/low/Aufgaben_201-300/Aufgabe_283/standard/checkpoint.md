Task: Add isFromProton(element: Element): boolean in mail helpers.
Status: Complete. Added strict IsProton === 1 check and optional IsProton fields to message, conversation, and encrypted-search message models. Added focused tests.
Verification: Mail Jest elements.test.ts passed (21 tests); mail TypeScript check passed; git diff --check passed.
Constraints: Local repository only; git history/index and harness config untouched.
