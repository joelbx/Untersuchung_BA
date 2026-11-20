VERDICT: FIX

**Code defect:** [topics.js](/app/src/controllers/write/topics.js:14) stores posting locks in a process-local `Set`. [loader.js](/app/loader.js:116) can start multiple workers, so overlapping requests from the same user can reach different workers, both acquire a lock, and create duplicate topics. Use an atomic lock shared across workers, with safe release, and verify the concurrent request case across workers.

**Tests:** `./node_modules/.bin/mocha test/topics.js --grep "should accept only one concurrent topic creation"` passed (1 test), and `./node_modules/.bin/mocha test/topics.js` passed (230 tests). Both ran in one worker and do not cover the defect.

**TEST_ENVIRONMENT_PROBLEM:** The first focused run failed before any test with `ECONNREFUSED 127.0.0.1:6379`. Starting the installed local Redis service allowed both commands above to pass. I made no project code or test changes during this independent review.