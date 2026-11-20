Updated Ubuntu lifecycle data: 20.04 has extended support through 1 April 2030, and 22.04 is recognized with standard support through 1 April 2027 and extended support through 1 April 2032. Ubuntu 22.04 can also pass the Gost CVE support check.

Added tests for the dates, lifecycle transitions, and release lookup. `go test ./config ./gost` and `git diff --check` passed.