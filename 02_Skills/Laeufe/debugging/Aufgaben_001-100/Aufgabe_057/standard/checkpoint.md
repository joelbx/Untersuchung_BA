# Checkpoint

Task: implement YAML-native variant attachment import and export in internal/ext.

Status: investigating repository interfaces, fixtures, and existing tests before editing implementation.

Checks: pending.

Root cause: cmd/flipt/export.go defines Variant.Attachment as string and copies the stored JSON verbatim; cmd/flipt/import.go sends that string verbatim to CreateVariant. The requested internal/ext package and fixtures do not exist in this checkout. Store methods already return nested variants, distributions, and constraints. The CLI implementations provide a complete working hierarchy pattern to adapt.

Hypothesis: changing the YAML model attachment to interface{}, decoding stored JSON before YAML serialization, and normalizing YAML maps before JSON encoding on import will preserve nested values and support omitted attachments.

Implemented: internal/ext shared YAML document model, paginated exporter with JSON attachment decoding, importer with recursive YAML map normalization and JSON encoding, and CLI delegation to the new APIs. Missing attachments are omitted on export and passed as empty strings on import. Existing JSON string attachments remain accepted.

Verification: initial `go test ./internal/ext -run 'TestAttachmentRoundTrip|TestImportWithoutAttachment' -count=1` failed as expected with undefined NewExporter/NewImporter before implementation. After implementation, `go test ./internal/ext ./cmd/flipt -count=1` passed; `go test ./...` passed; `git diff --check` passed. The referenced internal/ext/testdata fixtures are absent from this checkout, so exact fixture text comparison was unavailable; focused tests verify YAML structure and JSON round trip instead.
