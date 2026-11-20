Fault-localization progress:
- lib/events/dynamoevents/dynamoevents.go event.Fields is string; all three write paths serialize JSON, and session/search read paths decode it.
- Existing RFD24 migration provides locking via backend.RunWhileLocked, consistent Scan, batches of 25, retries, and progress logging. Completion uses an index marker; a FieldsMap migration needs its own marker.
- lib/backend/helpers.go has no FlagKey. backend.Key in lib/backend/backend.go creates separator-prefixed keys.
- SDK default encoder turns empty strings and empty maps/lists into NULL, so naive JSON-to-map conversion can lose semantics. Existing DynamoDB tests require AWSRunTests.
No project source or tests changed.
