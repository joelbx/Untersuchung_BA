Updated the album, artist, and share timestamp fields to represent unset values safely. Added `gg.P` and `gg.V`, and updated timestamp writes and reads to use them. A database migration replaces existing null `image_files` values with empty strings, addressing the scan error in the log.

The relevant package tests and database tests passed.