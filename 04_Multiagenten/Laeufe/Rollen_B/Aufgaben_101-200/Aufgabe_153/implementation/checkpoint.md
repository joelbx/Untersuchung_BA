Started: inspect share member/invitation stores and view; verify share isolation diagnosis, implement fix, run local tests.
Verified: both store copies hold global arrays; view fetches by share ID but reads/writes unscoped arrays. Implementing keyed state and scoped view actions.
Implemented share-keyed member and internal/external invitation maps in both copies; view now resolves and reads a specific share, and passes shareId to mutations. Validating types and adding isolation tests.
Complete: both source copies updated and identical where applicable. Added two store isolation tests; Jest passes (2 tests), package TypeScript check passes, git diff --check passes.
