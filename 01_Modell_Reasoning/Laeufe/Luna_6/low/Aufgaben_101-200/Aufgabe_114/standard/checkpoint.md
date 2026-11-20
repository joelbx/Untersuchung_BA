# Checkpoint

Task: implement local `artist.*` image discovery from artist album media directories, with per-attempt duration tracing.

Implemented album media directory lookup, artist image search in those directories before external URL and placeholder fallbacks, and elapsed trace fields for each artwork source attempt.

Verification: `go test ./core/artwork ./model` passed.
