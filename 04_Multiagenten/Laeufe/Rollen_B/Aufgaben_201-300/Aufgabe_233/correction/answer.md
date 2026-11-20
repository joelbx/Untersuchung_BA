Fixed `loadDir` so it no longer assumes an `fs.FS` directory implements `fs.ReadDirFile`. It retains the existing partial-read behavior where available and uses `fs.ReadDir` otherwise, returning an error if directory listing is unsupported. Added tests for both fallback cases.

`go test ./scanner` and `go test ./utils` pass. No remaining failures or test environment problems.