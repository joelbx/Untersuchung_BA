# Checkpoint

Root cause: the SSE broker published messages without sender identity and sent each message to every subscriber. The UI also had no per-window identifier in requests, leaving EventSource without an origin to compare.

Added client ID context, header/cookie middleware, per-window UI UUID, sender-aware broker messages, selective delivery, and regression tests. `go test ./...`, `npm run check-formatting -- --loglevel=error`, and `git diff --check` passed.

UI build attempt: `CI=true npm run build` failed with `ERR_OSSL_EVP_UNSUPPORTED` from webpack's `createHash` under Node.js v20.19.1. This was an offline tooling compatibility issue. `NODE_OPTIONS=--openssl-legacy-provider CI=true npm run build` passed. No build uncertainty remains.
