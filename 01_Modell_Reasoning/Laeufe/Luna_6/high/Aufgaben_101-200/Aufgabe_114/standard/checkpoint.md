# Checkpoint

Task: Find and prefer a local `artist.*` image in the artist folder before external artist image sources, expose album media directories, and trace lookup durations.

Implemented:
- `model.Album` now carries a non-persisted `Dirs` field, populated with unique media directories when built from `MediaFiles`.
- Artist artwork derives an artist folder from the associated album media directories and checks `artist.*` there before external files, URLs, and placeholders.
- Artwork source attempt trace logs include elapsed duration, on both successful and unsuccessful attempts.

Validation: `go test ./core/artwork ./model` passes; `git diff --check` passes.

Repository note: `rg` is unavailable, so standard filesystem and source inspection tools were used.
