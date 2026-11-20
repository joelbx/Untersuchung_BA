# Checkpoint

Task: Prefer local `artist.*` image from the artist folder, retain each album's unique media directories, and trace lookup durations.

Implemented: album media directories persist via `media_file_dirs` and are available through `Album.Dirs()`; migration forces a full rescan to populate existing albums. Artist image lookup checks the shared parent of album directories and the directory containing tracks before external files, URLs and placeholder. Each source attempt logs its duration.

TDD: Observed the album directory test fail because the field was absent; observed the artist image preference test choose an external file; observed duration log test report zero durations; observed the no-album-subfolder test choose the placeholder. All pass after implementation.

Verification: `GOPROXY=off GOSUMDB=off go test ./model ./core/artwork ./db ./persistence ./scanner -count=1` passed. `git diff --check` passed. `GOPROXY=off GOSUMDB=off go test ./...` ran, but failed in `scanner/metadata/taglib`: `correctly parses metadata from all files in folder` and `correctly handle unreadable file due to insufficient read permission`. The process runs as root and can read the fixture marked unreadable, yielding 3 files rather than 2 and no read error. All other packages in that run passed. TagLib emitted a C++ deprecated-method compiler warning.
