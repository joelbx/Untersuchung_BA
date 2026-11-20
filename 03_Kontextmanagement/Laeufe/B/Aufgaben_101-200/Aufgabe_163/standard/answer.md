Implemented separate database credential fields with protocol validation, default ports, and URL precedence. Connections and migrations now resolve the target from the same configuration, and parsing and connection errors avoid exposing credentials.

Verified with `go test ./config ./storage/db ./cmd/flipt`.