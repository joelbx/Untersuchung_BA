Implemented the gRPC version interceptor and added it to the server’s unary chain. It reads `x-flipt-accept-server-version`, accepts both `v1.0.0` and `1.0.0` formats, stores the parsed version in context, and falls back to 1.0.0 when the header is missing or invalid.

Added tests for parsing, fallback, and context retrieval. Both relevant Go test packages passed, and `git diff --check` passed.