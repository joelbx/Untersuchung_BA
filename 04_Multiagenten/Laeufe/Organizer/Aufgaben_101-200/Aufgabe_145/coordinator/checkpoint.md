# Recovery issue checkpoint

Status: complete.

Updated both Drive recovery hook copies and their focused tests. Recovery loads regular and trash listings, waits for both to decrypt, merges only photo files from the restored share, counts callback and rejected move failures, and checks both sources before success. Persisted in-progress recovery still resumes automatically.

Verification: both focused recovery test suites pass (11/11 each); ESLint passes on the four edited files. The drive-store type check fails in unrelated packages/crypto/lib/worker/api.ts because the installed openpgp and pmcrypto openpgp types differ.

Delegation: none.
