Added an explicit `disabled` field to each evaluation response. Batch evaluation now returns an ordered entry for every flag, marks disabled flags, and continues evaluating the rest. The existing batch test also verifies that the status survives protobuf JSON serialization.

Both test commands flagged by the reviewer passed, as did `git diff --check`. TEST_ENVIRONMENT_PROBLEM: none.