# Checkpoint

Task: Prefer local `artist.*` in the artist folder, expose album media directories, and trace lookup durations.

Implementation: Album media directories are persisted and exposed through `Album.Dirs()`. The scanner records them during album refresh. Artist artwork derives the shared parent of each album's media directories and checks `artist.*` there before external files, URLs, and placeholder. Every attempted source logs its elapsed duration. A migration adds `album.media_file_dirs` and forces a rescan to populate existing albums.

Verification: `GOPROXY=off go test -count=1 ./persistence ./model ./core/artwork ./scanner ./db ./db/migration` exited 0. The first run after adding a persistence test failed because the test changed a shared fixture; cleanup was added and the fresh run passed. `rg` was unavailable (`/bin/bash: rg: command not found`); local shell searches were used. Scanner emitted an existing TagLib deprecation warning.
