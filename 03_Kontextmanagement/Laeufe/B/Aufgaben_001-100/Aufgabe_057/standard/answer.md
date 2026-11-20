Implemented YAML-native variant attachments in [internal/ext](/app/internal/ext/common.go) and connected the CLI import and export commands to the new package. Attachments export as YAML structures and import as JSON strings; missing attachments remain optional.

The attachment round-trip test and existing storage tests pass.