# Checkpoint

Implemented runtime MIME configuration:
- Moved prior audio/image MIME mappings and lossless extensions into `resources/mime_types.yaml`. The resource is embedded and supports overrides from the configured data directory's `resources` folder.
- Added `mime` package loading through `conf.AddHook`; it registers configured MIME mappings, explicitly registers `.js` and `.css`, and exposes configured lossless extensions without leading periods.
- Updated the server UI configuration and its existing test to use `mime.LosslessFormats`.
- Ensured model MIME lookups link the hook package, and removed the old definitions from `consts/mime_types.go`.

Validation:
- `go test ./server ./mime` passed.
- `go test ./model ./server` passed after linking the MIME hook from model MIME lookups.
- `go test ./...` found the same two unrelated TagLib metadata assertion failures in `scanner/metadata/taglib`; all other output showed the model package's earlier MIME registration failure, which was fixed and verified with the focused run.
- `git diff --check` passed.
