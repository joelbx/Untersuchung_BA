Updated both synchronized recovery hooks to process regular items and trashed photo entries together. Recovery now waits for both sources to decrypt, tracks move failures and remaining items, waits for cache updates before declaring success, and resumes when persisted state says it was in progress.

Both focused suites pass (**15/15 tests each**); ESLint, Prettier, and whitespace checks pass. Workspace type checking remains blocked by an unrelated OpenPGP type mismatch in [api.ts](/app/packages/crypto/lib/worker/api.ts:579).

I delegated test expansion and an implementation review to two native agents, then integrated and verified the changes.