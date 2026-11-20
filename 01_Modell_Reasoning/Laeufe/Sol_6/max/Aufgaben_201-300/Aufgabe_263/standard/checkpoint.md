# Checkpoint

- Task: store DynamoDB audit event metadata as native `FieldsMap`, migrate legacy `Fields` JSON safely, and retain compatibility during migration.
- Repository: `/app`; initial worktree clean. Located event storage in `lib/events/dynamoevents` and backend flag helper in `lib/backend/helpers.go`.
- Implemented: new event writes use native `FieldsMap`; reads accept both formats. Conversion preserves empty values and decimal numbers, validates a round trip, and migrates with bounded batch writes under a distributed lock. A backend `.flags` key records completion.
- Added unit coverage for map content, legacy reads, invalid JSON, stable pagination, and `FlagKey`; added an AWS suite migration case for more than one batch.
- Verification complete: offline `GOPROXY=off GOSUMDB=off go test -mod=vendor -count=1 ./lib/events/dynamoevents ./lib/backend` passed; `git diff --check` and `gofmt -l` were clean. AWS-dependent integration coverage was added but could not run without the repository's AWS test setting.
