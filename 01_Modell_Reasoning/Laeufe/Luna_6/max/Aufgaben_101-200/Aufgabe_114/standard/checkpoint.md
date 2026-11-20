# Checkpoint

Task: Prefer an `artist.*` image in a folder derived from the artist's album media directories and log each artwork source attempt duration.

Implemented:
- Added transient `Album.Dirs`, populated from unique media file directories.
- Hydrated directories for stored albums when constructing an artist artwork reader and derived the artist folder from the common parent of each album's media directories, including multi-directory albums.
- Checked local `artist.*` images before existing image files, URLs, and placeholders.
- Added elapsed time to trace logs for directory scanning and every artwork source attempt.
- Included local artist directory and image timestamps in the artist image cache identity, including resized artwork, so cached external images do not mask local files.

Verification: `go test ./core/artwork ./model ./scanner ./persistence` passes. `git diff --check` passes.
