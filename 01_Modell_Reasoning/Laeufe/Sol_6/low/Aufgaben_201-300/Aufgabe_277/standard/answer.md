Updated the audit models so `Rule` and `RolloutSegment` include the optional JSON operator fields. Their constructors now copy a single segment key or join multiple keys with commas and record the operator. Existing legacy keys remain supported.

The audit package tests and the new focused segment tests pass.