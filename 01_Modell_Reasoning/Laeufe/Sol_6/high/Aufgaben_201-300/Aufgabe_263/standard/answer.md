DynamoDB audit events now store metadata in the native `FieldsMap` attribute. Reads accept both `FieldsMap` and legacy `Fields` during migration.

The [migration](/app/lib/events/dynamoevents/fieldsmap_migration.go) scans records in bounded pages, validates each conversion, and uses conditional updates to avoid overwriting changed events. It can resume after interruption and runs under distributed locks. I also added [FlagKey](/app/lib/backend/helpers.go) and conversion tests.

`go test ./lib/events/dynamoevents ./lib/backend -count=1` and `git diff --check` passed. The AWS dependent integration suite requires its opt-in environment setting, so it did not run.