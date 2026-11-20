Updated the EOL data for Fedora 37, 38, and 40; SUSE Enterprise Desktop and Server 13 and 14; and macOS 11 and 15. Appended the requested Windows KB mappings for builds 19045, 22621, 22631, and 20348 in revision order, using named struct literals.

Updated the existing tests and added EOL boundary and kernel version KB checks. `go test ./config ./scanner` and `git diff --check` passed.