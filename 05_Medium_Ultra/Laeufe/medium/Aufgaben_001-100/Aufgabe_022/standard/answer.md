Updated the RPM scanner to keep binary package metadata and append a warning when a source RPM filename cannot be parsed. Source filenames with an epoch now produce the expected source version and retain the link to the binary package.

Added tests for both reported filenames and for scan continuation. The focused scanner tests and `git diff --check` passed.