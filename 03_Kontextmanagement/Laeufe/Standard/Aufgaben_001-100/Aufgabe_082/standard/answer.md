Fixed the auth service crash when `stdout://` is combined with another audit backend. `stdout://` now uses `WriterEmitter`, and `MultiLog` validates and fans out typed audit events.

The event package tests, the existing service configuration test, and `git diff --check` passed.