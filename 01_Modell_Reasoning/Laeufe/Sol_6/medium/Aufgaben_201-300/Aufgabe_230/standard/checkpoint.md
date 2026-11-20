Task: Update affiliate queue identifiers to support ISBN and ASIN, deduplicate by identifier, and serialize all queue fields.
Status: Implemented PrioritizedIdentifier, compatibility wrapper, identifier-based deduplication, complete serialization, and staging-aware batch processing. Focused tests added.
Verification: Affiliate server tests passed (19 tests before final ordering test); lint and git diff check passed. Final test run pending.
