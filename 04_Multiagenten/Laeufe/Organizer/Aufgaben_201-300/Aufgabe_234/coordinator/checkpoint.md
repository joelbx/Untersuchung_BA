# Checkpoint

Task: Simplify SQLite access to one *sql.DB.
Decision: The issue's final requirement and INTERFACES section demand a read/write split, contradicting the title, problem, expected behavior, and first four requirements. The checkout already has the unified connection, so preserve that architecture.
Changes: Configure required SQLite DSN options in db.Db(); remove persistence's global database fallback for transactions and builders; make play-tracker writes use the transaction store; add DSN and transaction-routing regression tests.
Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./db ./persistence ./cmd ./core/... ./server/...` passed. After adding the play-tracker fix and test, `GOTOOLCHAIN=local GOPROXY=off go test ./db ./persistence ./core/scrobbler` passed. `git diff --check` passed.
Delegation: none.
