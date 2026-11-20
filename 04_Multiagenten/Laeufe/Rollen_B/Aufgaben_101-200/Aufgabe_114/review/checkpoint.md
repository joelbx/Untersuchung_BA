VERDICT: FIX

CODE DEFECTS
- core/artwork/reader_artist.go:66-73 always takes the parent of the album media directory. For one album stored directly in /music/Artist, artistFolder returns /music, so /music/Artist/artist.jpg is missed. Check the media directory itself when it is the artist directory, and cover this layout.
- core/artwork/reader_artist.go:38-47 derives the artist cache key only from external info and album update times. scanner/refresher.go:100-103 only folds image times from album media dirs into album update time. Adding or replacing /music/Artist/artist.jpg therefore leaves the key unchanged and utils/cache/file_caches.go:109-119 serves the old cached image. Include the artist image timestamp or invalidate the artist key on change.
- core/artwork/reader_artist.go:106-115 accepts any regular artist.* file, including artist.nfo, before image files. Restrict candidates using model.IsImageFile (or image validation) so image fallback remains available.

TEST_ENVIRONMENT_PROBLEM: none.
Tests executed successfully:
- GOPROXY=off GOSUMDB=off go test ./model ./core/artwork ./scanner ./db/migration (all passed; migration package has no tests; taglib deprecation warning)
- GOPROXY=off GOSUMDB=off go test ./persistence ./db (both passed)
- git diff --check (passed)
