# Checkpoint

Task: Improve Message Composer room replacement notices and related reusable cancel/profile/reply UI per issue.
Status: Investigating local implementation and tests using assigned systematic-debugging process.
Constraint: External research unavailable. No dependencies will be downloaded.

Investigation: The tombstone branch in MessageComposer.tsx renders its status as a styled span and `<br/>`; the existing test checks only the CSS class. ReplyPreview.tsx renders "Replying" without a sender and an icon-only AccessibleButton with no accessible name. DisambiguatedProfile hardcodes a div, preventing inline use in the reply header. There is no shared icon cancel component.
Hypothesis: The missing semantics and context come from these rendering choices. A paragraph for the status, an inline-capable profile for reply context, and a labeled shared CancelButton address the root cause.
Reproduction: `./node_modules/.bin/jest test/components/views/rooms/MessageComposer-test.tsx --runInBand --silent` exited 1 after changing the test to require a paragraph: expected 1, received 0 at MessageComposer-test.tsx:64.

Implementation: MessageComposer tombstone status is now a paragraph within a status region; the replacement link has its own paragraph. Added reusable CancelButton with button semantics, accessible name, and CSS size property. ReplyPreview identifies the sender and uses the shared cancel control. SenderProfile/DisambiguatedProfile can render inline markup in this context. SearchBar and LinkPreviewGroup use the shared control. Added English strings and focused tests.
Verification: Jest focused messaging suite (7 suites, 29 tests) passed before the final status-role assertion. ESLint and Stylelint passed. `git diff --check` and JSON validation passed.
Type check limitation: `./node_modules/.bin/tsc --noEmit --jsx react --pretty false` exited 2 with five errors outside changed files: matrix-js-sdk/src/http-api.ts lines 830, 885, 886 (`IRequest.abort` absent); AliasSettings.tsx:144 and SecurityRoomSettingsTab.tsx:223 (`MatrixClient.getLocalAliases` absent). No changed-file type errors remained after fixing the CancelButton size prop collision.
Final verification: After adding the status role and assertion, targeted Jest (3 suites, 5 tests), ESLint for the changed composer/test, and `git diff --check` passed.
