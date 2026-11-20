# Fault localization progress

Inspected `detector/vuls2/db.go`, `db_test.go`, `export_test.go`, and `vuls2.go`.

- `shouldDownload` returns immediately for `SkipUpdate` after the file stat, before opening the DB or reading metadata. A present DB with an incompatible schema is silently accepted in that mode.
- Otherwise it opens the DB and obtains metadata, handles retrieval errors and nil metadata with the path, but never compares `metadata.SchemaVersion` with `db.SchemaVersion`. The recent-download and last-modified branches can suppress a required refresh.
- `newDBConnection` constructs a read-only DB after the optional fetch and returns it without metadata validation. Its `Config.New` error also omits the path. `Detect` opens the returned DB afterwards.
- Existing `Test_shouldDownload` covers missing DB, freshness, and skip-update with matching schema only. There is no mismatch or `newDBConnection` test in this directory.

Likely fix location: `detector/vuls2/db.go`. Check schema mismatch before any skip/freshness return, and validate metadata in `newDBConnection` while preserving the returned connection's expected lifecycle. Error paths should identify the configured file.
