# Voice broadcast liveness issue

Status: complete.

Implemented unified `VoiceBroadcastLiveness`, explicit header call-site values, grey badge styling, playback liveness derived from playback and info state with change-only events, hook subscription, and final-chunk detection. Added focused model/UI/helper assertions and updated playback UI snapshots.

Verification: six focused Jest suites passed (75 tests, 9 snapshots); the LiveBadge suite also passed earlier (making seven suites overall). ESLint on changed TypeScript files, Stylelint on badge CSS, and `git diff --check` passed. Repository TypeScript check is blocked by the existing unrelated error at `src/utils/notifications.ts:79` (TS2554, three arguments where one or two expected).

Delegation: none.
