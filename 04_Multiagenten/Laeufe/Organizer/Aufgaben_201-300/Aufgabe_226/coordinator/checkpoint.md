Task: Externalize MIME types and lossless formats into mime_types.yaml.
Status: Complete. Added embedded/overridable resources/mime_types.yaml and mime package startup hook; removed consts MIME file; migrated UI configuration; documented override path.
Validation: GOPROXY=off go test ./mime ./server ./core ./model ./server/subsonic passed. git diff --check passed.
Delegation: None.
