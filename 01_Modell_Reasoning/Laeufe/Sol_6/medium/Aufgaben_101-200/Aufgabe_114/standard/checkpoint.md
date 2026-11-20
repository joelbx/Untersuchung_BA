# Checkpoint
Task: prefer artist.* from an artist's local folder and trace each lookup duration.
Status: complete.
Changes: album media directories are persisted through a migration and scanner refresh; artist folder is derived from the album directories; local artist image is checked before existing fallbacks; cache keys track local image metadata; every image source attempt logs its duration.
Validation: go test ./model ./core/artwork ./db ./persistence ./scanner; git diff --check.
