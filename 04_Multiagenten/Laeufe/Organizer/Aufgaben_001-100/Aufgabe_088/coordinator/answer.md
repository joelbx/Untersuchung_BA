Added optional `fields` selection to `getObject` and `getObjects` across Redis, MongoDB, and Postgres. An empty or omitted array returns the full object, including through `getObjectFields` and `getObjectsFields`. Selected reads include missing fields as `null`, preserve input key order, and return falsy values for missing objects.

The Redis hash suite passed **59 tests**. ESLint and `git diff --check` passed. MongoDB and Postgres integration tests could not run because those services were unavailable.

No delegation was used.