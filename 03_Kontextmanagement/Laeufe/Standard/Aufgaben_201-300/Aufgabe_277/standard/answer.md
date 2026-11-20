Updated the rollout audit structures and constructors to record segment keys and operators. Single segments use their key; multiple segments use comma-separated keys and include the operator. The new JSON fields are omitted when empty.

The audit and Kafka tests pass, and `git diff --check` is clean.