Artist artwork now checks for `artist.*` in the folder derived from the artist’s albums before trying the existing image sources. Albums persist their unique media directories, and every image lookup attempt records its duration in trace logs. The database migration triggers a full rescan to populate the new directory data.

Tests passed: `go test ./model ./core/artwork ./scanner ./persistence`.