Fixed the telemetry state issues. New or repaired identities now get a valid RFC3339 timestamp that allows an immediate first ping, and malformed JSON is logged before the state is regenerated. Added regression tests for both cases.

The reviewer’s exact test command passed, as did `git diff --check`. No remaining failures or `TEST_ENVIRONMENT_PROBLEM`.