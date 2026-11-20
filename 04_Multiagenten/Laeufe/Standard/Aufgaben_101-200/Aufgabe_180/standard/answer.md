Updated the EOL data for Fedora 37, 38, and 40; added SUSE Enterprise 13 and 14 dates; and marked macOS 11 ended while keeping versions 12–15 present. Extended the Windows 10, Windows 11, and Server 2022 KB mappings in revision order with named struct literals, and updated tests for EOL dates and kernel based KB detection.

Validation passed: `go test ./config ./scanner` and `git diff --check`.