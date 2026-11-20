Updated the nullable album, artist, and share fields so unset database values can be loaded safely. Added `gg.P` and `gg.V`, updated timestamp reads and assignments, and added regression assertions for unset fields.

The affected package tests pass, and `git diff --check` passes. The full suite has four failures in unchanged TagLib tests involving metadata expectations and file permissions.