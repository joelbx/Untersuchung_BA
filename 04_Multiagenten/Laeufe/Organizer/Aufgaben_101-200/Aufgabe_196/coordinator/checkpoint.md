# Checkpoint

Task: centralize Scribe addon resolution in assistant upsell config, normalize planIDs, and use payments/core public exports.
Status: implementation complete in checked-out files.
Changes: removed duplicate addon mapping; paid configs conditionally add resolved Scribe addon; payments/core exports SelectedPlan and getScribeAddonNameByPlan; external consumers use public imports; added unsupported-plan regression cases.
Validation: assistantUpsellConfig.test.ts passed (11 tests); git diff --check passed. Components type check blocked by pre-existing OpenPGP dependency type mismatch at packages/crypto/lib/worker/api.ts:577.
Delegation: none.
