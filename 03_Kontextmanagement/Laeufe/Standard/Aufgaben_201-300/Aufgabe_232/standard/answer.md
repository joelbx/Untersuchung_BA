Implemented OS EOL lookup and scan summary warnings. Scans now report expired support, available extended support, approaching EOL dates, and missing lifecycle mappings. OS family constants and major version parsing are centralized.

Relevant tests pass: `go test ./config ./util ./scan ./report ./oval ./gost`.