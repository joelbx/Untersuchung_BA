Implemented local artist image lookup in the artist folder derived from album media directories. The lookup checks `artist.*` before existing image files, URLs, and placeholders. Album directories are hydrated from media file paths, and local directory and image timestamps are included in the cache identity so stale cached artwork won’t bypass the local lookup.

Trace logs now include elapsed time for directory scans and artwork source attempts.

Verified: `go test ./core/artwork ./model ./scanner ./persistence` and `git diff --check` pass.

Changed: [album model](/app/model/album.go), [media file aggregation](/app/model/mediafile.go), [artist reader](/app/core/artwork/reader_artist.go), [artwork sources](/app/core/artwork/sources.go), [image cache](/app/core/artwork/image_cache.go), and [resized artwork](/app/core/artwork/reader_resized.go).