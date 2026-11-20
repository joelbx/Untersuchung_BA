# Checkpoint

Issue: Prefer an `artist.*` image in the artist folder derived from album media directories, and trace image lookup durations.

Completed:
- Added transient unique media directories to albums assembled from media files.
- Populated those directories from stored media files when constructing an artist artwork reader.
- Derived the artist folder from album media directories and checked its `artist.*` files before existing fallbacks.
- Added elapsed time to trace logs for every attempted artwork source.
- Existing suites passed: `go test ./core/artwork ./model` and `go test ./persistence ./scanner`.
