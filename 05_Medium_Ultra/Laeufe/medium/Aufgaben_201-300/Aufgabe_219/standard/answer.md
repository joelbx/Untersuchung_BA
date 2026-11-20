Token creation and deletion now produce audit events when their configured event pairs are enabled. The checker recognizes `token` and includes it in resource wildcards; gRPC initialization passes the resolved settings to the authentication services. Deletion events are emitted only after a successful deletion.

Relevant tests and `git diff --check` pass.