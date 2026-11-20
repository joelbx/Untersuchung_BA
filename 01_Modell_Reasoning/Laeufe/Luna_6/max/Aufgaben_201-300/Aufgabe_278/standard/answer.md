Implemented the mailbox reload and freshness changes.

- [useElements.ts](/app/applications/mail/src/app/hooks/mailbox/useElements.ts:97) now passes page and params to the loading selector, observes `pendingActions`, and waits for the count to reach zero before loading.
- [elementsActions.ts](/app/applications/mail/src/app/logic/elements/elementsActions.ts:17) separates delayed retries for request failures and stale responses. [elementQuery.ts](/app/applications/mail/src/app/logic/elements/helpers/elementQuery.ts:47) carries the API’s `Stale` flag through the result.
- [elementsReducers.ts](/app/applications/mail/src/app/logic/elements/elementsReducers.ts:28) tracks backend action lifecycles and retry state. The guard now covers mailbox mutations, draft saves, sends, deletes, and related refreshes.

Validation passed: TypeScript check, ESLint, 29 mailbox tests, and 14 composer sending tests. One composer test was skipped.