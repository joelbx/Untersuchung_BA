Updated the repository to handle unset timestamps safely. Album, artist, and share timestamp fields now accept NULL; the new `gg.P` and `gg.V` helpers preserve zero values and make nil reads safe. A migration also converts legacy NULL `image_files` values to empty strings, addressing the reported scan error.

The relevant Go package tests passed.