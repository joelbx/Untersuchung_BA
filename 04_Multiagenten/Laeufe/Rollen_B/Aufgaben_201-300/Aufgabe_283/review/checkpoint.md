VERDICT: FIX

Code defect: The issue's VerifiedBadge interface is missing at applications/mail/src/app/components/list/VerifiedBadge.tsx. Existing badge rendering in applications/mail/src/app/components/list/Item.tsx:107 still uses a sender address whitelist, and ItemColumnLayout.tsx:132 renders an inline image without the specified tooltip. Add the specified component and connect badge visibility to isFromProton where applicable.

The isFromProton helper itself performs the required strict IsProton === 1 check for Message and Conversation; its new tests cover 1, 0, and absent values.

Relevant existing tests executed:
- `yarn workspace proton-mail test src/app/helpers/elements.test.ts --coverage=false`: PASS, 1 suite, 22 tests.
- `yarn workspace proton-mail check-types --pretty false`: PASS (exit 0).
- `git diff --check`: PASS (exit 0).

TEST_ENVIRONMENT_PROBLEM: none.
