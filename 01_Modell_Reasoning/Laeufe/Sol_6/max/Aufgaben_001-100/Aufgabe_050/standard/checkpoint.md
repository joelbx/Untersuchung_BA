# Progress checkpoint

- Task: fix nullable timestamp handling and related database scan errors after the 0.51.0 upgrade.
- Repository: `/app`; initial working tree was clean. Edited checked-out files only; no git history or index changes.
- Added `gg.P` and `gg.V`. Album and artist external-info timestamps, share expiration and last-visit timestamps, and album image-file/path fields now represent SQL NULL with nil pointers. Updated scanner, artwork, external metadata, share, and Subsonic callers.
- Added database round-trip tests for NULL and present values, plus generic helper tests.
- Relevant package tests pass: `GOPROXY=off GOTOOLCHAIN=local go test ./utils/gg ./model ./persistence ./core ./core/artwork ./scanner ./server/public ./server/subsonic`.
- Full `go test ./...` fails only in four existing `scanner/metadata/taglib` tests due to the local TagLib output and root-readable permission fixture. All other packages in that run passed.
