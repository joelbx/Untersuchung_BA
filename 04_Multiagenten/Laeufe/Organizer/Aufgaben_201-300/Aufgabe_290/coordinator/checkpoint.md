Task: Fix muted legacy call sounds and expose stable sound IDs and media event listener.
Status: Complete. Exported AudioID; unmute immediately before every play, including queued replay after load; added handleEvent for media event logging and regression tests.
Verification: LegacyCallHandler test suites: 17 passed; TypeScript noEmit: passed; ESLint changed files: passed; git diff --check: passed.
Delegation: none.
