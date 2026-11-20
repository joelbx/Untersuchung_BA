Updated `Validate` to return a single error that unwraps into individual issues with file, line, and column. It now catches unknown rule variants and segments, including segments used by boolean rollouts.

`flipt import` validates before creating resources, so retrying an invalid file reports the same error. Both exported snapshot constructors validate files as they load them.

The affected tests pass: `go test ./internal/cue ./internal/storage/fs ./internal/ext ./cmd/flipt`.