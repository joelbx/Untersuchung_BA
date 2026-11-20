# Checkpoint

Task: fix stale bypass filter entries for optimistic mark-as actions.
Implemented: pass markAsStatus, classify affected elements by active read/unread filter, add or remove derived IDs in the reducer.
Verification: 3 Jest suites passed (13 tests); mail TypeScript check passed; Prettier check passed.
