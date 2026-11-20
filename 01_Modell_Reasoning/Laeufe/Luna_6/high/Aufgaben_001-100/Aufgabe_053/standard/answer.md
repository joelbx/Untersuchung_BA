Added an early return so `major("")` returns `""`, and added an empty-input case to `Test_major`.

Both `go test ./oval` and `go test ./oval -run '^Test_major$' -count=1` passed. The builds emitted an existing warning from the SQLite C dependency.