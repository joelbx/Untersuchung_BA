Updated the assistant upsell flows to use the shared Scribe addon resolver and return a `planIDs` object that includes the addon only when one applies. Payments/core now exports the resolver and `SelectedPlan`, and external call sites use that public entrypoint.

The assistant upsell suite passed: **11 tests**. The components type check remains blocked by an existing OpenPGP dependency type mismatch in `packages/crypto/lib/worker/api.ts:577`.

No delegation was used.