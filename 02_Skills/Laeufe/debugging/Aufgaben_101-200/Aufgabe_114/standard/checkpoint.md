# Checkpoint

Task: find local `artist.*` in an artist folder before external artist image sources; expose album media directories and trace lookup durations.

Status: investigating repository and reproducing the issue. `rg` is unavailable (`/bin/bash: rg: command not found`); using local fallback search.

Investigation: `newArtistReader` only collects `Album.ImageFiles`, which lists images in media directories. `selectImageReader` then tries that list and the external source. No album media directory is persisted, so `artist.*` in the parent artist directory cannot be found when the album has no listed image. The scanner already computes unique media directories with `MediaFiles.Dirs()`.

Hypothesis: Persisting those directories on each album, then deriving the common artist base from associated albums, lets a local `artist.*` lookup precede external sources. A focused regression test was added and is running before the fix.

Reproduction: `go test ./core/artwork -run TestArtwork -ginkgo.focus='prefers artist artwork' -count=1` failed as expected: returned `artist-placeholder.webp` instead of the local `artist.jpg`. A second pre-fix test showed identical cache keys before and after a local image appeared.

Implemented: album media directories are persisted by the scanner and exposed through `Album.Dirs()`; a migration adds the column and forces a rescan. The artist reader computes a shared folder from associated albums, checks local `artist.*` first, and uses the local file metadata in the cache key. The shared selector and local folder scan trace durations.

Verification: `go test ./core/artwork ./model ./scanner ./persistence ./db/migration -count=1` passed (exit 0). `git diff --check` passed. The scanner emitted a TagLib C++ deprecation warning but the check passed.
