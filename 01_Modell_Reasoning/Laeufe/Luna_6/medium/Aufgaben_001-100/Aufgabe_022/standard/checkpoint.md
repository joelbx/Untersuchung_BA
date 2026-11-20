# Checkpoint

Task: Resolve RPM source filename parsing failures, including non-standard SOURCERPM warnings and epoch-aware parsing.

Changes: Invalid source RPM filenames now emit a warning and are skipped while binary package metadata is returned. `splitFileName` recognizes an epoch prefixed to the source RPM name and includes it in the parsed version; source package construction avoids duplicating that epoch. Applied the same tolerant handling to the repoquery parser.

Verification: `go test ./scanner` passed.
