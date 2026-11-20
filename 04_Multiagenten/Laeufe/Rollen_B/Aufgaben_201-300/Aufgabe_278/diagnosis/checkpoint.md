# Fault localization progress

Inspected the mailbox hook, elements state/actions/reducers/selectors/query helper, existing mailbox element tests, and representative item mutation hooks. No project source or tests modified.

Findings:
- `useElements.ts` calls `loadingSelector(state)` without `{ page, params }` (line 99). Its main effect (116-129) has no pending backend operation count or guard, so reset/load/page updates can run while item mutations remain active.
- `elementsActions.ts` load thunk (23-43) directly returns `queryElements`; there is no stale response check. Its error timer dispatches `retry` at 2 seconds, but `elementsSlice.ts` does not register `retry`, and no rejected-load reducer clears `pendingRequest`. This can strand loading after a failure.
- `elementQuery.ts` (41-47) discards API `Stale`; `QueryResults` in `elementsTypes.ts` (86-90) has no `Stale` field. A stale response therefore reaches `loadFulfilled` (51-68) and commits total, pages, and elements.
- `ElementsState` and `newState` have no `pendingActions`; selectors have no accessor. The `loading` selector (184-187) omits `shouldSendRequest`, so it misses requests implied by current page/params.
- No `backendActionStarted`/`backendActionFinished` dispatches appear under `applications/mail/src/app`. Representative label/move/mark/delete hooks do run async API work; wiring action lifecycle dispatches to these or a shared wrapper appears necessary for the counter to reflect real work. Exact integration scope remains uncertain.
- Existing `Mailbox.elements.test.tsx` covers pagination/placeholders but does not cover stale results or fetch failure retry.

Behavior to cover: defer list reload until all overlapping backend item operations finish; clear pending request and retry failures after 2s with bounded count; reject `Stale === 1` without committing it and retry after 1s; maintain loading for current page/params until valid data arrives. Avoid letting a stale-response throw also schedule the generic error retry.
