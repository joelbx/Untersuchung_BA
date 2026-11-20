VERDICT: FIX

**Code defects**

- [reader_artist.go](/app/core/artwork/reader_artist.go:66) always searches the parent of an album’s media directory. If tracks are stored directly in `/music/Artist`, it misses `/music/Artist/artist.jpg`. Check the media directory as a candidate too.
- [reader_artist.go](/app/core/artwork/reader_artist.go:38) leaves the artist cache key unchanged when a parent-folder `artist.*` is added or replaced, so the cache can keep serving the old image. Include that file’s timestamp in invalidation.
- [reader_artist.go](/app/core/artwork/reader_artist.go:106) accepts files such as `artist.nfo` as artwork. Filter candidates with `model.IsImageFile` so valid images and fallbacks remain reachable.

**TEST_ENVIRONMENT_PROBLEM:** None.

Tests executed: `GOPROXY=off GOSUMDB=off go test ./model ./core/artwork ./scanner ./db/migration` and `GOPROXY=off GOSUMDB=off go test ./persistence ./db` passed. The migration package has no tests. `git diff --check` passed.