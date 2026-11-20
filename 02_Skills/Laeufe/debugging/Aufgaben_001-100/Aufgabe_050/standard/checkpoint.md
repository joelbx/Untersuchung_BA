# Checkpoint

Investigating the reported nullable timestamp scan failures and related model fields. No fix chosen yet.

## Tooling
`rg` is unavailable (`/bin/bash: rg: command not found`); using local `find` and `grep`.

## Root cause and hypothesis
SQLite migrations declare `album.image_files`, `album.external_info_updated_at`, `artist.external_info_updated_at`, and `share.expires_at` nullable. The corresponding model fields are nonpointer string/time.Time. Persistence uses dbx `.One`/`.All` to scan directly into model fields; database/sql cannot scan NULL into a string or time.Time. The reported `image_files` error is the first encountered NULL, and timestamp columns share the same mismatch. Hypothesis: pointer fields permit NULL scanning, while `gg.P`/`gg.V` make writes and reads explicit. Comparable working pattern: nullable fields use pointer semantics in model (inspection continues).

## Pattern analysis and verification
Existing nullable timestamps in `model.User` and `model.Playlist` use `*time.Time`. The album artwork and share consumers previously assumed plain values. A focused dbx scan regression reproduced the exact `image_files` NULL error before the fix. After making the reported nullable fields pointers, the same regression exposed NULL `last_visited_at`; that field is now a pointer too. Reads use `gg.V`, and assignments use `gg.P` when a value is present, including an intentional zero timestamp for scanner refresh.

Verification: `go test ./utils/gg ./persistence ./core ./core/artwork ./scanner ./server/public ./server/subsonic -count=1` passed. `go test ./... -run '^$'` passed (compile only). The TagLib C++ compiler emitted an existing deprecation warning, without failing either check.
