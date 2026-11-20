Implementing YAML-native variant attachments; inspecting current CLI workflows and store APIs.
Verified existing CLI owns schema and workflows; adding internal/ext with shared YAML representation, JSON attachment conversion, and CLI wiring.
Implemented internal/ext schema, batched export, import, recursive YAML map normalization, and CLI delegation. Focused round-trip tests pass; cmd/flipt compiles. Named fixtures are absent in this checkout.
Added explicit-null attachment presence tracking so JSON null exports as YAML null and imports back as JSON null; missing attachments remain empty. Final focused tests and diff check pass.
