Updated the album, artist, and share models so optional timestamps can be null, and made album `image_files` nullable to address the reported scan error. Added `gg.P` and `gg.V` and updated the affected read and write paths.

The relevant Go tests and `git diff --check` pass. A broader run failed in unrelated TagLib fixture and file-permission tests.