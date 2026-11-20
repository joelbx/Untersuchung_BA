Updated the RPM scanner so an unparseable `SOURCERPM` adds a warning while preserving the binary package and allowing the scan to continue. Source filenames with an epoch now produce the correct source name and version, with the binary link retained. The Amazon repoquery path handles both cases as well.

Regression tests and the full `./scanner` test suite passed.