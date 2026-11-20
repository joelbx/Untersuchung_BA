# Checkpoint

- Added `config.EOL`, strict-after phase evaluators, centralized family constants, and canonical EOL mappings for all requested family/release pairs.
- Added `config.GetEOL`, including Amazon Linux 1/2 handling and release normalization for major or major.minor OS identifiers.
- Added `util.Major`; config distro parsing, OVAL, and GOST now use the centralized major-version parser.
- Scan result assembly appends standardized EOL warnings (excluding pseudo and Raspbian); scan summary renderers preserve warning order and print EOL warnings with the `Warning: ` prefix.
- Verified existing packages with `go test ./config ./util ./scan ./report ./gost ./oval` (all passed).
