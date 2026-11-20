# Checkpoint

Task: prevent rapid repeat activation of Kick, Ban, and Mute actions in the room member user info panel.

Implementation: `src/components/views/right_panel/UserInfo.tsx` now uses a synchronous guard scoped by room and member, plus shared pending state so all available admin action buttons are disabled with `aria-disabled="true"`. The lock is acquired before confirmation/warning dialogs and released in `finally` after cancel, success, or failure. API failures continue to produce one error dialog. Updating-count callbacks use functional state updates so the spinner count stays balanced.

Verification: the focused `UserInfo-test.tsx` suite passes (68 tests), ESLint passes for the changed file, and `git diff --check` passes. The full TypeScript check still fails on existing dependency/SDK errors in other files; it reports no errors in `UserInfo.tsx`.
