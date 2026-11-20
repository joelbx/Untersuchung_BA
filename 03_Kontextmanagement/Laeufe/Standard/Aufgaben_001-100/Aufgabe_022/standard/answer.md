Updated RPM parsing so an unparseable `SOURCERPM` adds a warning while preserving the binary package and allowing the scan to continue. Epoch-prefixed source filenames now produce the correct source name and version, linked to the binary package.

Added regression tests for both cases and the repoquery path. The focused scanner tests passed.