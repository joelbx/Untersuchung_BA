Artist artwork lookup now checks for `artist.*` in the folder derived from the artist’s albums before trying external files, URLs, or a placeholder. Albums persist their unique media directories, and every artwork source attempt records its duration in trace logs.

Tests passed: `go test ./model ./core/artwork ./db ./scanner` and `go test ./persistence`.