Task: Prevent duplicate admin actions in the user info panel.
Status: Complete. Added shared per-member lock across Kick, Ban, and Mute; lock begins on activation and releases after confirmation cancellation or operation settlement. Added regression test for cross-action rapid clicks and cancellation.
Verification: UserInfo Jest suite passed (69 tests); Prettier and git diff --check passed. Full tsc has unrelated existing dependency and repository errors; a newly introduced UserInfo type error was corrected.
Constraints: Used local repository only; preserved git history, index, and harness configuration.
