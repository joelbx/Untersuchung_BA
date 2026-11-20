Restored legacy `listenPorts` parsing as a string list and moved structured scan data to `ListenPortStats`. Updated port parsing, destination selection, reachability matching, and report display, with tests for legacy JSON and the new interfaces.

`go test ./models ./scan ./report` and `git diff --check` passed.