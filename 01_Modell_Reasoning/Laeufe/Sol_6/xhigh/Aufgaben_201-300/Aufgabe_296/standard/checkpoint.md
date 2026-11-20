Task: Allow registration with an invitation token and no email, while preserving invitation email confirmation, group membership, inviter tracking, and cleanup.

Progress: Implemented token-based invitation metadata, per-email token sets, inviter references, token-only verification, email confirmation on matching invite email, group joining, and complete invitation cleanup. Restored the registration form's query-token handling and allowed token-only registration past the email interstitial. Preserved tokens through approval queue acceptance.

Verification: 33 invitation tests, 6 approval queue tests, and 2 register page controller tests pass. ESLint, JavaScript syntax checks, and `git diff --check` pass. Tests used a temporary local Redis instance because no Redis server was listening initially.
