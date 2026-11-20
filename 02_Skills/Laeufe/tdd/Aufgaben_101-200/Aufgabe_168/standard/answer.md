Fixed the user info panel’s Kick, Ban, and Mute controls. The first activation immediately sets `disabled` and `aria-disabled="true"` on all three buttons for that member. They stay inactive through confirmation and the operation, then re-enable on success, cancellation, or failure. A failure shows one error dialog.

The [user info tests](/app/test/components/views/right_panel/UserInfo-test.tsx) pass (70/70), including rapid clicks, keyboard activation, cancellation, and failure recovery. Scoped lint and formatting pass.

The full suite has 5 failures in unrelated TimelinePanel, OIDC, and StopGapWidget tests. Type checking also reports errors outside the changed files. Details are in the [checkpoint](/app/.codex-role-output/checkpoint.md).