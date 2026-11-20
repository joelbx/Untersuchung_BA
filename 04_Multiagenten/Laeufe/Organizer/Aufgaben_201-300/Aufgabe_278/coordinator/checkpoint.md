# Checkpoint

Task: Fix mailbox element list reload timing, retries, and stale response handling.
Status: Complete.
Implemented: backend operation counter and lifecycle dispatch in mutation hooks; guarded mailbox and encrypted search loads; ignored in-flight responses received during mutations; added timed generic and stale retries; propagated Stale; corrected loading selector context.
Verification: mail TypeScript check passed; ESLint on changed files passed; 12 mailbox tests passed; 3 lifecycle tests passed; git diff --check passed.
Delegation: none.
