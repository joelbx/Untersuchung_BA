Added a `user_props` table and a context-scoped `UserPropsRepository`, then switched LastFM session keys to use it. The migration moves existing LastFM keys out of the global property table. LastFM property error logs now include a request ID when available.

`go test ./...` passed. The build emitted SQLite and TagLib compiler warnings.