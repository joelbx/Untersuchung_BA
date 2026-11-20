# Checkpoint

Issue: replace outdated assistant upsell addon selection with the centralized Scribe addon resolver, unify planIDs construction for single- and multi-user configs, and use public payments/core exports.

Progress: centralized resolver and SelectedPlan are exported from the public payments/core entry point. Assistant upsell now uses the resolver, both paid config builders support an optional addon, and assistant module imports use the public entry point. The relevant existing Jest suite passed (9 tests). Final diff and import checks completed; no remaining assistant imports reference the internal subscription path.
