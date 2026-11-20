Implemented OS EOL lookup, per-target scan warnings, and ordered `Warning: ...` lines in the scan summary. OS family constants and major-version parsing are now centralized.

Verified with `go test ./config ./scan ./report ./util ./oval ./gost`; all passed.