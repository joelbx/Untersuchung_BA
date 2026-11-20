Implemented the `fanoutbuffer` package in [buffer.go](/app/fanoutbuffer/buffer.go) with configurable defaults, concurrent cursors, blocking and nonblocking reads, close notifications, backlog cleanup, and grace-period errors.

`go test ./fanoutbuffer` passed; the package currently has no existing tests.