Updated the album, artist, and share models so nullable timestamps and album `image_files` can be read without database scan errors. Added public `gg.P` and `gg.V` helpers and updated callers to preserve optional values and read nil timestamps as zero values.

The affected package tests and `git diff --check` passed. No delegation was used.