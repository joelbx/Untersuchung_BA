Fixed stale bypass entries in `/app`. Mark-as actions now pass their status to the reducer, which removes an element’s bypass ID when its new status matches the active Read or Unread filter. Added regression tests for both filters and conversation mode.

Verification: 10 relevant tests passed; TypeScript, Prettier, and `git diff --check` passed.