Task: support discrete database credentials with URL precedence in /app.
Status: implementation complete and verified.
Changes: added config.DatabaseProtocol enum and database fields; field-qualified validation and driver URL resolution; URL-safe parsing and connection errors; shared connection path for application and migrations; migrations take config by value; pooling applied in both modes; default config documentation and tests updated.
Verification: GOPROXY=off go test ./... passed; git diff --check passed.
Constraints respected: no external research/downloads, no git history/index/harness changes.
