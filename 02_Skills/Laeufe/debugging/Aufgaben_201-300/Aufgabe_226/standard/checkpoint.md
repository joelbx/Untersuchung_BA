# Checkpoint

Investigating MIME initialization and lossless format references before editing source. `rg` is unavailable in this environment; using `find` and `grep` for repository inspection.

Root cause: `consts/mime_types.go` registers mappings at package init and derives `consts.LosslessFormats` from hardcoded maps. `conf.Load` runs hooks after config fields are set. `resources.FS()` merges embedded resources with `DataFolder/resources`, so a `resources/mime_types.yaml` resource can provide bundled defaults and operator overrides. UI currently reads the consts list.

Hypothesis: moving registration into a `mime` startup hook that reads `resources.FS()` will make both MIME lookup and the UI list reflect runtime YAML. Test with an override containing a custom extension and lossless entry.

The first broader run had two failures: `go test ./server` could not compile because the updated test retained an unused `strings` import (removed), and `go test ./model` reported `IsAudioFile("test.m3u")` true. Root cause of the model failure: its test binary imports `model` but not the new `mime` package, so `mime.init` never registers the startup hook before `tests.Init` calls `conf.LoadFromFile`. Importing the loader from `model/file_types.go`, where MIME detection occurs, registers the hook for that entry point.

Implemented: moved default mappings and lossless extensions to `resources/mime_types.yaml`, added `mime` hook to read the merged embedded/override resource at config load, removed `consts/mime_types.go`, and switched UI to `mime.LosslessFormats`. `model/file_types.go` imports the loader so the hook is registered wherever model MIME functions are used.

Verification: regression test initially failed to build (`undefined: LosslessFormats`) before implementation. After implementation, the first MIME test failed only because Go appends `charset=utf-8` to text MIME types; its assertion was corrected. The first broad test run failed on an unused server-test import and on model's `m3u` expectation due to the missing package import; both causes were addressed. Final passing commands: `GOPROXY=off go test ./mime ./model ./server ./core -count=1`; `GOPROXY=off go test ./cmd ./server/subsonic ./scanner -count=1`; `git diff --check`.
