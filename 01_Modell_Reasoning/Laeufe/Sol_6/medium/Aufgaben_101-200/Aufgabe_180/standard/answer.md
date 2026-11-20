Updated the EOL data for Fedora 37, 38, and 40; SUSE Enterprise Desktop and Server 13 and 14; and macOS 11 and 15. Extended the Windows 10 22H2, Windows 11 22H2/23H2, and Server 2022 KB mappings in revision order using named struct literals. Tests now cover the updated dates and kernel version KB detection.

`go test ./config ./scanner` and `git diff --check` pass.