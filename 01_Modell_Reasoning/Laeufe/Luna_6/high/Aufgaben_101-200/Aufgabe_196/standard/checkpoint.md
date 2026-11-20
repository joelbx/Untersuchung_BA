# Checkpoint

Task: Resolve the assistant upsell addon resolver inconsistency in `/app`.

Initial action: Locate the upsell config helpers, central Scribe addon resolver, payments/core exports, and relevant existing tests. Then implement the requested shared `planIDs` behavior and run relevant existing tests.

Progress: The assistant upsell now uses `getScribeAddonNameByPlan`; both paid config helpers construct `planIDs` with optional addon entries. Exported `SelectedPlan` and the resolver from the public payments/core entry point, and updated direct `SelectedPlan` imports to use it. The existing assistant upsell test passed (9 tests). Final checks: inspect diff and verify no remaining internal `SelectedPlan` imports or legacy resolver references.
