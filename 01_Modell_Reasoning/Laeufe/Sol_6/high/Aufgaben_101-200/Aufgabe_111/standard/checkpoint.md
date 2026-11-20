Task: Add Amazon Linux 2023 and later release detection and EOL support.
Status: Implemented normalized version parsing for 1, 2, 2022, 2023, 2025, 2027, and 2029; added EOL dates; corrected system-release parsing, OVAL release selection, and ALAS2023 source links.
Verification: GOPROXY=off GOSUMDB=off go test ./config ./scanner ./oval passed. git diff --check passed.
Next: Coordinator can export the checked-out file changes.
