# Checkpoint

Implemented photo recovery enumeration across restored regular photos shares and volume trash. Recovery waits for decryption in each source, merges trashed image/video items by their actual source share, tracks combined move progress, checks both sources before success, marks core promise failures as failed while accounting for remaining targets, and resumes persisted `progress` state.

The mirrored `packages/drive-store` and `applications/drive` hook and existing hook tests were updated. Existing hook tests pass after resetting queued mock implementations between tests. Package type checking was attempted but is blocked by an unrelated OpenPGP type mismatch in `packages/crypto/lib/worker/api.ts:579`. Final targeted test, lint, and diff checks are in progress.
