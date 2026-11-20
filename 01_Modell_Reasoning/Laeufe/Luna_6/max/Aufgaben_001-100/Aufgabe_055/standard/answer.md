Implemented the Trivy metadata and detector changes.

- The parser records `Metadata.OS.Name` in `Release`, uses `ArtifactName` for `ServerName`, adds `:latest` to untagged container images, and clears `Optional` in [parser.go](/app/contrib/trivy/parser/v2/parser.go:38).
- Package CVE detection now logs skip reasons for missing or unsupported metadata, skips Trivy results, and logs and returns OVAL/GOST errors in [detector.go](/app/detector/detector.go:209). Trivy reuse checks `ScannedBy` in [util.go](/app/detector/util.go:24).
- Updated parser expectations in [parser_test.go](/app/contrib/trivy/parser/v2/parser_test.go:203).

Verification passed: `go test ./contrib/trivy/parser/v2 ./detector` and `git diff --check`.