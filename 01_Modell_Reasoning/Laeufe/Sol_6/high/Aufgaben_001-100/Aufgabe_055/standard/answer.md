Updated the Trivy v2 parser to store the OS name in `Release`, use `ArtifactName` for `ServerName`, append `:latest` to untagged container images, and leave `Optional` nil. Package CVE detection now skips Trivy and the specified unsupported cases; CVE reuse identifies Trivy scans through `ScannedBy`.

The parser and detector tests pass: `go test ./contrib/trivy/parser/v2 ./detector`.