Updated the RPM scanner so an unparseable source filename adds a warning while the binary package remains available. Source filenames with an epoch now produce the correct source name and version, linked to the binary package.

Focused and full `./scanner` tests passed.