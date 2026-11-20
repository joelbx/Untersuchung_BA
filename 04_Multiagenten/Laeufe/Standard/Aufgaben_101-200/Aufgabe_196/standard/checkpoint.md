# Checkpoint

Task: centralize Scribe addon resolution in assistant upsell configuration, normalize planIDs, and use payments/core public exports.
Status: complete.
Changes: exported SelectedPlan and getScribeAddonNameByPlan from payments/core; removed duplicate assistant addon mapping; built paid planIDs conditionally; updated external imports; added unsupported-plan coverage.
Verification: assistant upsell and selected-plan Jest suites passed (50 tests); Prettier check and git diff --check passed.
