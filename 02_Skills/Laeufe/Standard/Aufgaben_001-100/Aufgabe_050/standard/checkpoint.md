# Checkpoint

Task: Fix nullable album, artist, and share timestamp reads after upgrade, plus the reported nullable album image_files scan.
Status: Implemented and verified in checked-out files.
Changes: Added generic gg.P and gg.V; made album external_info_updated_at/image_files, artist external_info_updated_at, and share expires_at/last_visited_at nullable; updated assignments and reads; added helper and NULL-scan regression tests.
Checks passed: `GOPROXY=off go test ./utils/gg ./model ./persistence ./core/... ./scanner ./server/subsonic/... ./server/public/...`; `git diff --check`.
Broader check: `GOPROXY=off go test ./utils/gg ./model ./persistence ./core/... ./scanner/... ./server/subsonic/... ./server/public/...` failed in scanner/metadata/taglib because its fixture enumeration included test_no_read_permission.ogg, its m4a gain tag output contained duplicate values, and root could read an unreadable fixture. The initial run also had artwork fixture compile errors, which were fixed before the passing focused run. TagLib failures are unrelated to this change; its package was excluded from the passing focused run.
