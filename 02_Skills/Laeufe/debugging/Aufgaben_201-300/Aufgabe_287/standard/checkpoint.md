# Checkpoint

Task: add album image path tracking through scanner, model, and migration.

Assigned skill: systematic debugging.

## Root cause and pattern
`loadDir` records only `HasImages`, discarding names. `MediaFiles.ToAlbum` has no scan directory data, and `refresher.refreshAlbums` persists its result without image paths. `Scan` processes changed folders while still receiving directory results, so its map is incomplete for albums spanning later directories. Existing migration helper `forceFullRescan` clears scan timestamps and is used by the latest migration. Existing model fields use `structs` and `json` tags; ORM maps columns by field names.

Hypothesis: retaining image names in `dirStats`, passing the complete directory map to refreshers, and deriving album paths from sorted unique media directories fixes both full and incremental refreshes. A migration must add `album.image_files` and force a full rescan.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.

## Implementation and verification
Added `dirStats.ImageFiles` collection, `MediaFiles.Dirs()`, `Album.ImageFiles`, the album image path helper, and complete directory-map propagation to changed/deleted directory refreshers. Changed folder processing now starts after traversal finishes. Added a migration with a non-null default for existing albums and `forceFullRescan`.

Regression tests were written first and failed as expected on missing `Dirs`, `ImageFiles`, and helper symbols. After the patch, `GOPROXY=off go test ./model ./scanner ./persistence ./db/... -count=1` passed (exit 0). `git diff --check` passed. TagLib emitted a pre-existing C++ deprecation warning during compilation.
