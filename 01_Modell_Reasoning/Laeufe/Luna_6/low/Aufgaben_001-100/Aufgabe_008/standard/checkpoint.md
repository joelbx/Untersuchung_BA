# Checkpoint

Task: prevent repeated API requests for recently failed Drive link fetches, scoped by `(shareId, linkId)`.

Plan:
- Inspect `useLink.ts` and its existing tests for error handling and API conventions.
- Add a short-lived internal cache for the specified client-visible error codes.
- Extend focused existing tests if appropriate, then run the existing targeted test command.
