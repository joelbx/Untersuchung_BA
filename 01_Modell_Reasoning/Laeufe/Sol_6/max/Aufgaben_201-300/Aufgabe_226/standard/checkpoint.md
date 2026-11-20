# Checkpoint

Task: externalize MIME mappings and lossless format definitions into `mime_types.yaml`, load them at startup, and update consumers.

Status: implemented `resources/mime_types.yaml`, a `mime` package that loads it through `conf.AddHook`, updated MIME and lossless consumers, removed `consts/mime_types.go`, and added a resource override test. Tests passed: `go test ./mime ./model ./core ./server ./server/subsonic` and `go test ./cmd` with network access disabled.
