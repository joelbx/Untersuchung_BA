Task: Fix rollout audit models so Rule and RolloutSegment carry segment operators and constructors aggregate segment keys.
Status: Updated audit types and constructors; added legacy, single, multiple, and JSON omission tests. Audit package suite is compiling/running.
Constraints: Use local code/tests only; preserve git history, index, and harness configuration. Restore incidental go.work.sum changes after test.
