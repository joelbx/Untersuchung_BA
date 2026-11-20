MIME configuration now loads from [mime_types.yaml](/app/resources/mime_types.yaml) at startup through `conf.AddHook`. The server uses `mime.LosslessFormats` for its uppercase, comma-separated UI value. The resource can be overridden at runtime from the data folder’s `resources` directory.

Relevant Go tests and `git diff --check` passed.