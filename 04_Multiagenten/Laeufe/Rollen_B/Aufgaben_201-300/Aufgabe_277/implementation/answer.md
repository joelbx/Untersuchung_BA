Updated the audit `Rule` and `RolloutSegment` structures with the requested JSON fields. Their constructors now preserve single segment keys and rollout values, and join multiple keys with commas while recording the operator name. Added tests for those cases and JSON omission when the operator is empty.

The audit and Kafka package tests passed with network access disabled.