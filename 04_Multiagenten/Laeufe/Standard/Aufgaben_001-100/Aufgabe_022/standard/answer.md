Updated the RPM scanner so an unparseable `SOURCERPM` adds a warning and skips only the source package; the binary package remains available and the scan continues. Epoch-prefixed source filenames now produce the correct source name and version, linked to the binary package.

Added regression tests and verified with `go test ./scanner -count=1`.