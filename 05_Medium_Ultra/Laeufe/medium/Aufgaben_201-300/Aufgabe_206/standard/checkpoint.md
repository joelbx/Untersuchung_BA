# Checkpoint

Task: prevent overlapping topic creation requests by the same actor from creating duplicate topics.
Status: implemented and verified.
Changes: added `Topics.lockPosting` with actor key and a posting lock around create/reply; added a concurrent API regression test checking HTTP responses and topic counters.
Verification: ESLint passed; focused concurrent test passed; guest create and reply regression cases passed (3 passing total). Local Redis was started for tests and stopped afterward.
