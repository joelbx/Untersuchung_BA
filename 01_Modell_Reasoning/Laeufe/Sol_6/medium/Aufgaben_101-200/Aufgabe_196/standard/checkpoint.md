# Checkpoint

Task: Resolve assistant upsell addon selection and planIDs consistency.
Status: Implemented and verified.
Changes: Exported SelectedPlan and getScribeAddonNameByPlan from payments/core; switched call sites to public entrypoint; removed duplicate addon mapping; built planIDs conditionally in paid single and multi user configs; added coverage for unsupported addon plans.
Verification: Assistant upsell Jest suite passed (11 tests); git diff --check passed.
