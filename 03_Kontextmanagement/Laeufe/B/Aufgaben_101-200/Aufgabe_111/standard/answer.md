Implemented Amazon Linux 2023 support in the checked-out repository. Release detection and version normalization now recognize 2023 and the specified later releases; EOL mappings, ALAS2023 advisory links, and OVAL lookup routing are updated. Unrecognized releases no longer fall back to Amazon Linux 1.

Validation passed: `go test ./config ./scanner ./oval ./models` and `git diff --check`.