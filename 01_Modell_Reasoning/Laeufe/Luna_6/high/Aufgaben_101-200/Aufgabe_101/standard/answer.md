Implemented array support for `listRemoveAll` across Redis, MongoDB, and PostgreSQL. Scalar removal remains supported, and the shared test covers duplicate occurrences, survivor order, and immediate read consistency.

ESLint passed. The database test could not run because Redis at `127.0.0.1:6379` refused the connection during setup.