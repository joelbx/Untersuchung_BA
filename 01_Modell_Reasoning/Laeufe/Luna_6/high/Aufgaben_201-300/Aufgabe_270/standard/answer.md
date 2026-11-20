Implemented the persisted session lookup and updated public session initialization, user localID retrieval, and telemetry to use the full session. Added focused tests for latest-session selection, empty storage, and storage access errors.

The focused Jest test passed. Type checking remains blocked by an unrelated OpenPGP `PartialConfig` type error in `packages/crypto/lib/worker/api.ts:579`.