Implemented `gg.P` and nil-safe `gg.V`, and made album/artist metadata timestamps and share expiration timestamps nullable. Updated timestamp reads and assignments to use the helpers.

Existing tests passed: `go test ./utils/gg ./model ./core ./scanner ./server/subsonic ./server/public`. `git diff --check` passed. The scanner build reported a TagLib deprecation warning.