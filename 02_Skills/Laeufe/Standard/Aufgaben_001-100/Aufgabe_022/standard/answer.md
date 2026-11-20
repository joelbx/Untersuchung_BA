Updated the RPM parser so an unparseable source filename adds a warning and skips only the source package; the binary package remains available and the scan continues. Source filenames with an epoch now produce the expected source name and version.

Added regression tests. The full scanner package test suite passed with offline dependencies.