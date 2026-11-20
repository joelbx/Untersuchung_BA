# Checkpoint

Implemented local artist image lookup and timing traces.

- Albums now expose unique media directories, populated by `MediaFiles.ToAlbum()` and refreshed from media file records when constructing artist artwork.
- Artist artwork computes a shared artist folder from album media directories and tries a case-insensitive `artist.*` file there before existing external artwork, URL, and placeholder sources.
- Artwork source trace messages now include elapsed duration for successful and unsuccessful attempts.
- Added a regression test proving a local artist image wins.

Verification: `go test ./core/artwork ./model` passed; `git diff --check` passed.
