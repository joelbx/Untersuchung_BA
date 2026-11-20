# Checkpoint

Task: remove stale bypassFilter entries for optimistic mark-as actions.
Status: complete. Added status dispatch/type, helper and reducer removal path, regression coverage.
Verification: Jest elementBypassFilters and elementTotal suites passed; mail tsc --noEmit passed; Prettier and git diff --check passed.
Delegation: none.
