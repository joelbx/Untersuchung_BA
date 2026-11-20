Fixed the nullable field scan errors. Album image files and the affected album, artist, and share timestamps now use pointer fields. Added `gg.P` and `gg.V`, and updated the scanner, metadata, artwork, and sharing paths to handle absent values safely.

Added NULL scan and helper tests. The affected package tests pass, and `git diff --check` is clean.