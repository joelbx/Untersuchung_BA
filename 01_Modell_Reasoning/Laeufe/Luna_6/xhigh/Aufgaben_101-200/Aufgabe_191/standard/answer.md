Implemented registration-token support in [InteractiveAuthEntryComponents.tsx](/app/src/components/views/auth/InteractiveAuthEntryComponents.tsx:188). Both stable and unstable stage identifiers now use the token form, which submits the server’s advertised type and token. The existing auth flow continues to deliver successful responses with client secret and email SID metadata.

The view includes the labeled autofocus field, help text, accessible primary action, Enter and click submission, busy spinner, duplicate-submit guard, and accessible error alert.

**Validation:** 2 existing test suites passed (5 tests); ESLint, Prettier, and `git diff --check` passed. The full TypeScript check reports errors in unrelated Sliding Sync code, with none in the changed component.