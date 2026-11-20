# Checkpoint

Task: resolve repeated requests for consistently failing `(shareId, linkId)` fetches in Drive's `useLink` hook.

Plan: inspect hook and its existing tests, add a per-key short-lived cache for specified API errors, then run relevant existing tests.
