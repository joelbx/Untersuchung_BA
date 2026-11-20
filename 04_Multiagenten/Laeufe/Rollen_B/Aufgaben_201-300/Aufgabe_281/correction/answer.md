Fixed bulk increment validation so Mongo rejects forbidden field names, including `bad.field`, before normalizing them.

The reviewer’s targeted Redis tests passed: 4 bulk tests and 68 Hash methods tests. A direct local check confirmed Mongo field-name validation. **TEST_ENVIRONMENT_PROBLEM:** Mongo integration tests could not run because `mongod` is unavailable locally.