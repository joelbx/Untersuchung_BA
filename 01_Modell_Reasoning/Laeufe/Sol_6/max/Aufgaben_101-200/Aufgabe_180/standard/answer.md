Updated [OS EOL data](/app/config/os.go) for Fedora 37, 38, and 40; marked macOS 11 ended and added macOS 15. Extended the [Windows KB mappings](/app/scanner/windows.go) for builds 19045, 22621, 22631, and 20348, preserving prior entries and using named struct fields throughout.

The issue assigns the 13/14 cutoff dates to SUSE, but those versions are in the repository’s FreeBSD table. I updated FreeBSD 13/14 and left the existing SUSE entries intact.

The full config tests and targeted scanner KB tests pass.