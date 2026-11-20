Fixed Amazon Linux build-release handling. Releases such as `2023.0.20230322` now normalize to `2023` for EOL and OVAL lookups, while unsupported releases remain unknown. Added regression coverage for the scanner, version parser, EOL, and OVAL paths.

`GOPROXY=off GOSUMDB=off go test ./config ./oval ./scanner` passed.