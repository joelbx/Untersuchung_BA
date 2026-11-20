Implemented Trivy OS version parsing and artifact-based server names, including `:latest` for untagged container images. Trivy results no longer use `Optional["trivy-target"]`; detection now recognizes them through `ScannedBy` and skips unsupported package CVE scans.

The parser and detector tests passed, as did the full offline `go test ./...` suite.