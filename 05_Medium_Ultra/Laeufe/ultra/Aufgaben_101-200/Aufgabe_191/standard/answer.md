Implemented registration token support in [InteractiveAuthEntryComponents.tsx](/app/src/components/views/auth/InteractiveAuthEntryComponents.tsx:190). Both stable and unstable stage IDs now open a focused, labelled token form. Enter and the primary button use the same submission logic; the view submits only the advertised `type` and entered `token`, blocks duplicate submissions, and shows busy and error states. Added the help text and [focused tests](/app/test/components/structures/InteractiveAuth-test.tsx:20).

**Verification:** 14 tests pass across four auth and registration suites. ESLint and Prettier pass. The full TypeScript check still reports unrelated Sliding Sync SDK type errors.

I delegated the SDK flow audit and test coverage, then integrated and verified the final patch.