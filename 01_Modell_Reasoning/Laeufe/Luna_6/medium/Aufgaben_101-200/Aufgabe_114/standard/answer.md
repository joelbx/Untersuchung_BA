Implemented local artist image lookup in the computed artist folder, with existing artwork sources as fallbacks. Album models now expose unique media directories, and artwork trace logs include the duration of each source attempt.

Added a regression test confirming that a local `artist.*` image is preferred. `go test ./core/artwork ./model` and `git diff --check` passed.