Artist artwork lookup now checks the computed artist folder for `artist.*` before external files, URLs, and the placeholder. Albums retain their unique media directories, and a migration fills that data for existing albums. Each artwork source attempt now records its duration in trace logs.

Verified with `go test ./model ./core/artwork ./scanner ./persistence`.