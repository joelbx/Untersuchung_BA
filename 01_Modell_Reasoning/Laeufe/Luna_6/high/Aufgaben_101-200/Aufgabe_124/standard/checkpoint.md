# Checkpoint

Implemented configurable DynamoDB `billing_mode` with accepted values `pay_per_request` and `provisioned`, defaulting to `pay_per_request`. Table creation maps these values to the AWS SDK billing mode; on-demand creation omits provisioned throughput and provisioned creation uses configured read/write units.

Initialization now returns the discovered table billing mode with its status and skips configured autoscaling with an explanatory log for existing on-demand tables and tables created on-demand. Added focused tests for config validation/defaults, creation parameters, and table mode detection, and documented the configuration.

Validation: `go test ./lib/backend/dynamo` passed; `git diff --check` passed.
