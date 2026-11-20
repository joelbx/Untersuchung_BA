Updated the RPM parsers so an unparseable `SOURCERPM` adds a warning while the binary package remains available and the scan continues. Source filenames with a numeric epoch now produce the correct source name; the binary and source versions retain the epoch.

Added regression tests for both parser paths and scan continuation. Targeted scanner tests and `git diff --check` passed.