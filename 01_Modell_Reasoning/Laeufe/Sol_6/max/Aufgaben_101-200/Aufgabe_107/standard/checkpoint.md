# Checkpoint

- Task: remove stale mail bypass-filter entries when mark-as status matches the active read/unread filter.
- Repository: `/app`; working tree initially clean.
- Located the optimistic hook, action types, and reducer. The requested bypass helper does not yet exist.
- Implemented status-aware bypass add/remove logic in the hook, action type, reducer, and new helper.
- Added reducer regression coverage for both filters, conversation IDs, duplicate bypass entries, unrelated IDs, and missing bypass metadata.
- Verification: 2 focused Jest suites (8 tests), mail TypeScript check, targeted ESLint, and Prettier all passed.
- Final diff review complete; only the intended mail source and regression test files changed.
