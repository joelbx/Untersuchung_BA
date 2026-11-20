# Checkpoint

Task: centralize assistant upsell Scribe addon resolution, use `planIDs` in both paid flows, and expose shared payment utilities through `@proton/components/payments/core`.

Status: implementation updated. Removed the duplicate assistant addon mapping, exported the existing shared resolver and SelectedPlan from payments/core, switched consumers to that entrypoint, and made paid upsell plan IDs conditional on a resolved addon. Added tests for plans with no Scribe addon.

Verification: targeted assistant upsell and selected-plan Jest suites passed (50 tests). Prettier and `git diff --check` passed. The components type check reports one existing external type mismatch in `packages/crypto/lib/worker/api.ts:577` between the top-level and pmcrypto copies of openpgp; it reports no error in changed files.
