The RPM scanner now records a warning for an unparseable source RPM filename, keeps the binary package, and continues the scan. It also parses epoch-prefixed source filenames so the binary and source packages have the correct versions and remain linked.

Regression tests cover both behaviors and the repoquery path. `GOPROXY=off go test ./scanner -count=1` passed.