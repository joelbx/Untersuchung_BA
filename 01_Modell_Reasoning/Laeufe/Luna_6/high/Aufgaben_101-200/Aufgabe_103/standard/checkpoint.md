# Checkpoint

Implemented empty-release preservation, consistent epoch/version/release composition, source RPM `-src.rpm` parsing with empty or hyphenated releases, filename validation, and `(none)` update epoch handling.

Validation: `gofmt` and `git diff --check` pass. `go test ./scanner` completed but fails against existing expectations that package `Version` omits the release and that `-src.rpm` sources are invalid. Those expectations conflict with the requested behavior; the new parser follows the issue requirements. Several kernel selection expectations are also affected by the requested composed `Version` format.
