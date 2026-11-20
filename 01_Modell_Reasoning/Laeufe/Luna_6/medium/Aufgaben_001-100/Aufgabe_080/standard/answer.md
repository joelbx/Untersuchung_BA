Implemented square artwork support across the backend and album grid frontend. Square images are centered on a square canvas, PNG encoded, and cached with a distinct key. Non-square requests retain their original shape and format.

Verification passed: `go test ./core/artwork ./server/subsonic ./server/public` and `git diff --check`.