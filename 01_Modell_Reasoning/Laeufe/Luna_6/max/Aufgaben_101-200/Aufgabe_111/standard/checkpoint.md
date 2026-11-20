# Checkpoint

Task: Add Amazon Linux 2023/2025/2027/2029 version detection and EOL support.

Constraints: Work from checked-out repository code and existing tests only; do not alter git history, index baseline, or harness configuration.

Completed:
- Normalize only recognized Amazon Linux releases, mapping YYYY.MM releases to Amazon Linux 1 and unrecognized releases to `unknown`.
- Add standard support end dates for Amazon Linux 2023/2025/2027/2029; unknown releases remain absent from EOL results.
- Parse Amazon Linux system release lines for 2023 and preserve Amazon Linux 1/2/2022 parsing.
- Select matching Amazon Linux OVAL data sets and format ALAS2023 advisory links.
- Add regression tests for release normalization, scanner parsing, OVAL selection, EOL dates, and support boundaries.

Verification: `go test ./config ./scanner ./oval` passed.
