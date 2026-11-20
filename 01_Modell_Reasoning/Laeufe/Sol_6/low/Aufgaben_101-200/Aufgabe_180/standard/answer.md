Updated the OS EOL data for Fedora 37, 38, and 40, SUSE Enterprise 13 and 14, and macOS 11 while keeping macOS 12–15 present. Extended the Windows 10 22H2, Windows 11 22H2/23H2, and Server 2022 KB mappings in revision order using named struct fields, then updated the affected test expectations and added kernel-version detection checks.

`go test ./config ./scanner` and `git diff --check` pass.