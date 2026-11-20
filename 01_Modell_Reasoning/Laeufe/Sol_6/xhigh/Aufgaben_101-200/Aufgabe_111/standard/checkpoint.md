# Amazon Linux release support

- Located version normalization and EOL mapping in `config/os.go`.
- Found two additional AL2023 gaps: `/etc/system-release` parsing in `scanner/redhatbase.go` and Amazon OVAL release routing in `oval/util.go`. ALAS advisory links also only supported AL2022.
- Updated normalization, EOL dates, release parsing, OVAL routing, and advisory links.
- Added focused regression cases for normalization, EOL boundaries, scanner release parsing, OVAL release selection, and ALAS links.
- Final `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./config ./scanner ./oval` passed across all three packages.
- Also updated the `/etc/redhat-release` detection branch to recognize Amazon Linux when that file is present.
- Numeric build releases such as `2023.0.20230315.0` now normalize to the major release; legacy `YYYY.MM` values still normalize to Amazon Linux 1.
