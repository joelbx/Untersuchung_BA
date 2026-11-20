Implemented selective SSE delivery. Request events now reach only other sessions of the same user; background events still reach all subscribers. The UI sends a per-page UUID on its HTTP requests, and the EventSource reuses the HttpOnly cookie established by its keepalive request.

Updated the broker, request context, middleware, scanner and Subsonic event calls, cookie expiry constant, and diode API. Added tests for event filtering and client ID cookie handling.

**Verification:** `go test ./...`, the 41 UI tests, and UI lint passed. The production build could not complete: the repository’s Webpack 4 build fails on Node 20 with `ERR_OSSL_EVP_UNSUPPORTED`.