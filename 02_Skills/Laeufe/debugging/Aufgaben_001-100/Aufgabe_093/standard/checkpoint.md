# Checkpoint

Issue: Popper placement reporting in RTL.
Status: Investigating placement data flow and tests before editing implementation.
Constraints: Local repository only; no downloads, history, index, or harness changes.

Root cause: Floating UI uses the floating element's computed RTL direction to place top/bottom start/end visually, while usePopper returns Floating UI's logical `placement` unchanged. Consumers receive the opposite visual alignment in RTL.
Pattern: Existing custom middleware in popper/utils.ts returns derived values through `data`; usePopper already reads middlewareData for arrow and hidden state. Floating UI platform exposes `isRTL(elements.floating)`.
Hypothesis: A reporting-only middleware after placement-changing middleware can invert top/bottom start/end into middlewareData, and usePopper can expose that value without altering coordinates.

Reproduction: `../../node_modules/.bin/jest components/popper/utils.test.ts --runInBand --coverage=false --reporters=default` from packages/components failed before implementation because getInvertedRTLPlacement and rtlPlacement were undefined (18 new cases failed; 5 existing cases passed).
Fix: Added RTL normalization for top/bottom start/end and reporting middleware that uses `platform.isRTL(elements.floating)`. Hook now returns middleware's normalized placement while preserving Floating UI positioning.
Verification: Same focused Jest command passed (23/23). `../../node_modules/.bin/tsc --noEmit --pretty false -p tsconfig.json` from packages/components exited 0. `git diff --check` exited 0.
