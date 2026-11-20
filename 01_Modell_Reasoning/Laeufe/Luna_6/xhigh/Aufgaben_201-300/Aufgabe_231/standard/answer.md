Implemented schema validation in [db.go](/app/detector/vuls2/db.go:31). Database connection and metadata errors now include the database path; nil metadata and schema mismatches return explicit errors. `shouldDownload` forces a download for a mismatched schema, or returns an error when `SkipUpdate` is enabled.

`go test ./detector/vuls2` passed.