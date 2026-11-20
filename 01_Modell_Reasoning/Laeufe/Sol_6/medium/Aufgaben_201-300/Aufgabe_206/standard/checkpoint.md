Task: prevent concurrent topic creation by the same authenticated user from creating duplicates.
Status: implemented a per-user/session posting lock around topic creation and replies, with guaranteed release on completion or failure. Added a translated conflict error and a concurrent request regression test checking responses and topic counters.
Verification: ESLint passed for the edited JavaScript files. Focused concurrent test passed (1 passing), and the existing topic posting tests passed (14 passing) using a temporary local Redis instance.
