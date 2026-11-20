I localized the issue, but did not edit project source or tests: this run was constrained to fault localization.

[consts/mime_types.go](/app/consts/mime_types.go) contains every hardcoded mapping, the lossless list, and the current registration logic. The likely fix is to move those definitions to `resources/mime_types.yaml` and load them through [resources/embed.go](/app/resources/embed.go), whose resource filesystem supports an override in `DataFolder/resources`. Register the loader with `conf.AddHook`; [conf/configuration.go](/app/conf/configuration.go) runs hooks during startup after setting the data folder.

[server/serve_index.go](/app/server/serve_index.go) must read `mime.LosslessFormats` and continue emitting an uppercase, comma-separated `losslessFormats` value. Its [existing test](/app/server/serve_index_test.go) also references the old constant. Preserve the explicit `.js` and `.css` registrations.

The main uncertainty is how a missing or malformed YAML file should affect startup; the requirements do not specify that behavior. Existing tests cover the UI key and basic file classification, but not loading or overriding the YAML resource.