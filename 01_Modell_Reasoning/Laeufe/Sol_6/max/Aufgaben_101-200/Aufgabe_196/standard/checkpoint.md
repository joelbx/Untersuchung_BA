# Checkpoint

Task: Resolve assistant upsell addon selection and planIDs consistency in /app.

Initial state: Working tree clean. No AGENTS.md found. `rg` is unavailable, so repository searches will use local alternatives.

Implemented: Exported `SelectedPlan` and `getScribeAddonNameByPlan` from payments/core; migrated external call sites to that entrypoint; removed the duplicate assistant addon mapping; built optional-addon `planIDs` in paid flows; routed the free flow through the same resolver and builder.

Verification: Assistant upsell and SelectedPlan Jest suites passed (50 tests). Prettier, targeted ESLint, and `git diff --check` passed. Repository-wide search found no legacy addon resolver or `@proton/components/payments/core/subscription/` imports. Component typecheck failed on an unrelated OpenPGP type incompatibility at `packages/crypto/lib/worker/api.ts:577`; no diagnostics pointed to edited files.
