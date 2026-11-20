Resolved the lockfile path issue in `/app`. Each lockfile is analyzed separately, vulnerability details retain its path, report lookups use path and library name, and repeated CVEs keep findings from both files.

The affected package tests and focused multi-lockfile regression tests passed with network access disabled.