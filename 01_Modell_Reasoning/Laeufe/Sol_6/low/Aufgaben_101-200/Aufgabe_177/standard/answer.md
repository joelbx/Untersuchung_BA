Implemented chat allow and deny lists, an incoming chat disable setting, server-side permission checks for chat initiation and room creation, and an idempotent upgrade that seeds allow lists from follows. Account settings controls and relevant tests were updated.

Syntax checks passed. The targeted test run could not reach the tests because Redis at `127.0.0.1:6379` refused the connection.