The change is localized to [lib/backend/dynamo/dynamodbbk.go](/app/lib/backend/dynamo/dynamodbbk.go:49). `Config` lacks `billing_mode`; `createTable` always sends provisioned throughput and no billing mode; `getTableStatus` discards the billing mode returned by `DescribeTable`; and `New` enables autoscaling whenever configured.

A fix should default an omitted `billing_mode` to `pay_per_request`, validate both supported values, and send the matching AWS billing mode at creation. On-demand creation needs nil `ProvisionedThroughput` and must ignore configured capacity units. Initialization needs the existing table’s billing mode so it can skip autoscaling and log why for on-demand tables, including newly created ones.

The existing [autoscaling test](/app/lib/backend/dynamo/configure_test.go:55) assumes provisioned capacity without specifying it, so it would need an explicit `billing_mode: provisioned` when this behavior changes. I did not run the AWS-dependent tests.

I recorded the diagnosis in [checkpoint.md](/app/.codex-role-output/checkpoint.md). **No project source or tests were changed:** this run was restricted to fault localization.