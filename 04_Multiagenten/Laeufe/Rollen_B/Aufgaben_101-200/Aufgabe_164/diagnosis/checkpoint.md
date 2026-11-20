Fault localization findings:
- internal/ext/encoding.go uses yaml.v2 for both YAML decoding and encoding. Nested values in Flag.Metadata (map[string]any in internal/ext/common.go) can decode into map[interface{}]interface{}, which structpb.NewStruct rejects in internal/ext/importer.go:168. Nested variant attachments have a local convert workaround at importer.go:199,425; metadata has none.
- cmd/flipt/export.go:110 writes a leading '# exported ...' line plus a blank line to any named output, including JSON. internal/ext/encoding.go:49 passes JSON input directly to json.NewDecoder, which rejects '#'. Importer.Import constructs that decoder at importer.go:53.
- Namespace fields are represented by NamespaceEmbed and applied in importer.go:90-119 for non-default namespaces. Existing tests cover flat metadata, namespace counts, and normal JSON/YAML, but not nested metadata or JSON with a leading header.
- go.mod already includes yaml.v3 v3.0.1. No project source or tests modified.
