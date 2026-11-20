# Checkpoint

- Task: prefer `artist.*` in the artist folder, expose unique album media directories, and trace lookup durations.
- Status: complete. Albums persist unique media directories; artist artwork checks the derived folder first and updates cache keys for local image changes. Trace logs include lookup duration. The migration requests a full rescan to populate existing albums.
- Verification: `go test ./model ./core/artwork ./db ./persistence ./scanner` passed.
