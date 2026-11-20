Artist artwork now checks for `artist.*` in the folder derived from the artist’s albums before trying external files, URLs, or a placeholder. Albums persist their unique media directories, and every image source attempt logs its duration. Existing libraries will need a rescan to populate the new directory data.

`go test ./model ./core/artwork ./scanner ./persistence` passed.