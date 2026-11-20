# Checkpoint

Task: Prefer local `artist.*` images in the artist folder, expose album media directories, and trace lookup durations.

Status: Inspecting repository. `rg` is unavailable; using local `find`/`grep`.

Implemented so far: album media directories are persisted from scanner aggregation with a migration and full rescan; artist reader derives a shared folder and checks `artist.*` first; shared artwork source selection records elapsed duration.

Next: add focused tests and run relevant Go packages.

Verification: `go test ./model ./core/artwork ./db ./scanner` passed after removing an unused import. `go test ./persistence` passed. `git diff --check` passed. The scanner build emitted an existing TagLib deprecation warning.

Result: Local artist image lookup precedes external files, URLs, and placeholder. Album media directories are persisted and exposed by `Album.Dirs()`. Each artwork source attempt has an `elapsed` trace field.
