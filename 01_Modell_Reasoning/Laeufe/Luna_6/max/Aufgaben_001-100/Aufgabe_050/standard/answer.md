Implemented the nullable timestamp handling and legacy database fix.

- Added generic `P` and `V` helpers in [gg.go](/app/utils/gg/gg.go:4).
- Made album, artist, and share timestamps nullable, and updated reads and assignments to use `V` and `P`.
- Added a migration to replace legacy NULL `image_files` values with empty strings in [20261009120000_fix_null_image_files.go](/app/db/migration/20261009120000_fix_null_image_files.go:14).
- Updated the checkpoint at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).

The affected package tests pass. `go test ./...` had four failures in the existing TagLib suite, involving fixture metadata differences and file permission behavior; the other packages passed. `git diff --check` passes.