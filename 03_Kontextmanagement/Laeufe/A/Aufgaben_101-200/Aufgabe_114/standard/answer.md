Artist artwork now checks for a local `artist.*` image in the folder derived from the artist’s albums before trying external files, URLs, or a placeholder. Albums retain their unique media directories, and each artwork lookup attempt logs its duration.

The relevant model, artwork, scanner, and persistence tests pass.