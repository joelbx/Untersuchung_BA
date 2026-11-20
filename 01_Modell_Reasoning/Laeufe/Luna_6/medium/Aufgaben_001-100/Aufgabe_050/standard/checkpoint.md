# Checkpoint

Implemented nullable timestamp handling for album/artist external metadata timestamps and share expiration timestamps. Added generic `gg.P` and `gg.V` helpers; adjusted timestamp assignment and reads to preserve optionality and safely return zero values for nil pointers.

Validation: `go test ./utils/gg ./model ./core ./scanner ./server/subsonic ./server/public` passed. `git diff --check` passed. The scanner build emitted an existing TagLib deprecation warning.
