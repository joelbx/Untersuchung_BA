# Checkpoint

Implemented square artwork support across the artwork interface, resize/cache layer, Subsonic and public endpoints, and album grid URL generation. Square resized images use a centered image on an RGBA square canvas and PNG encoding; the square mode is part of the cache key. Non-square resized requests retain their source dimensions and PNG/JPEG encoding.

Verification: `go test ./core/artwork ./server/subsonic ./server/public` passed. `git diff --check` passed.
