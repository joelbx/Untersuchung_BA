# Checkpoint

Resolved assistant upsell configuration by using the shared Scribe addon resolver, constructing planIDs before returning each paid config, and exporting/importing SelectedPlan and the resolver through payments/core.

Verification: assistantUpsellConfig.test.ts passed (11 tests); Prettier check and git diff --check passed.
