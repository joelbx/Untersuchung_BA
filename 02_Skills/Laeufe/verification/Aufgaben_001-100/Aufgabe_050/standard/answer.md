Updated the nullable album, artist, and share timestamps to use pointers. Added `gg.P` and `gg.V` so writes preserve optional values and reads safely return a zero value for nil pointers. A migration also replaces legacy NULL `image_files` values that caused the reported album scan error.

The relevant Go package tests and `git diff --check` passed.