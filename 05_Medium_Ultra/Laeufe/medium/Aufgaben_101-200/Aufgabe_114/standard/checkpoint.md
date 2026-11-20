# Checkpoint

Task: prefer `artist.*` in the artist folder, retain album media directories, and trace lookup durations.

Completed: album records now persist unique media directories; a migration forces a rescan to populate existing records. Artist artwork checks the shared parent folder first and then uses the prior sources. Each source attempt logs its duration. Added model and artwork tests.

Verification: `go test ./model ./core/artwork ./scanner ./persistence` passed; `git diff --check` passed.
