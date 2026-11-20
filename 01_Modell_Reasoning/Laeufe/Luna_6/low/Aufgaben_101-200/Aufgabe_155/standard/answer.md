Implemented digest support across image configuration, scanning, and report naming. Image validation now requires exactly one of `tag` or `digest`, and full image references use `name@digest` or `name:tag`.

`go test ./config ./scan ./report` passes. `go test ./models` is blocked by existing go vet diagnostics in `models/library.go` involving integer-to-string conversions.