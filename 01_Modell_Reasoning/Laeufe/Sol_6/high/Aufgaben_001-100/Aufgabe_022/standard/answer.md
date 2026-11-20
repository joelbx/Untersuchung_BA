Updated the RPM scanner so an unparseable `SOURCERPM` records a warning while preserving the binary package and continuing the scan. Source filenames with an epoch prefix now produce the correct source name and epoch version, with the binary link intact.

The targeted scanner tests pass, including the new cases for both reported filenames and scan continuation. `git diff --check` also passes.