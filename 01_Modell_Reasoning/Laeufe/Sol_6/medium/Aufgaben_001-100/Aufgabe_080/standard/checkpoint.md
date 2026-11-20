# Checkpoint

Resolved AlbumGrid shaking with non-square artwork in the Navidrome checkout.

- Added `square bool` to artwork Get/GetOrPlaceholder and propagated it through internal calls, Subsonic, and public image serving.
- Square mode centers artwork on a transparent square RGBA canvas and encodes PNG; regular mode retains prior shape and format behavior. Cache keys include square mode.
- AlbumGrid requests square cover art through `getCoverArtUrl`; cache warmer preloads the square variant.
- Added regression tests for non-square JPEG sizing, PNG output and padding, cache key separation, and Subsonic flag parsing.
- The requested OCI Source interface cannot be implemented in this repository: no `internal/storage/fs/oci` package or corresponding types exist, and it is unrelated to this issue.

Verification: `GOPROXY=off GOTOOLCHAIN=local go test ./core/artwork ./server/subsonic ./server/public` passed; Prettier check passed; `git diff --check` passed.
