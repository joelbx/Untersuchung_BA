Updated the RPM parser so an unparseable `SOURCERPM` adds a warning while the binary package remains available and scanning continues. Epoch-prefixed source filenames now produce the correct source name and version, with the source linked to its binary package.

The scanner regression tests passed, including cases for both filenames. No delegation was used.