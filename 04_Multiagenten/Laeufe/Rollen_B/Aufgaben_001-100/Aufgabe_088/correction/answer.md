The existing patch implements field selection across MongoDB, Postgres, and Redis. The reviewer found no code defect, so I made no source changes in this correction round.

I started the local Redis test service and reran the exact flagged command: `./node_modules/.bin/mocha test/database/hash.js` — **57 passing, exit 0**. `git diff --check` also passed. MongoDB and Postgres tests were not run.