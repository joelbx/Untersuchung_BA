# Checkpoint

Task: simplify SQLite access to one *sql.DB connection.
Status: complete. Required SQLite DSN options configured; persistence uses its injected connection for transactions; transaction call sites use tx; focused tests added.
Verification: GOPROXY=off GOTOOLCHAIN=local go test ./db ./persistence ./server ./core/scrobbler ./core ./scanner ./server/nativeapi ./server/subsonic passed; git diff --check passed.
