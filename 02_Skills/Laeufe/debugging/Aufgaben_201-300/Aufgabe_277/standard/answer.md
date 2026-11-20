Updated [audit types and constructors](/app/internal/server/audit/types.go) so rules and rollouts record comma-separated segment keys and the operator for multiple segments. Single segment values remain supported, and the new operator fields are omitted from JSON when empty.

Added [regression tests](/app/internal/server/audit/types_segments_test.go). The audit and Kafka audit test suites pass.