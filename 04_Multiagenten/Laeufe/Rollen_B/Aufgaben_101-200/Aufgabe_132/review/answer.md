VERDICT: FIX

**Code defect:** [The add tags API](/app/src/controllers/write/topics.js:100) validates existing tags alongside newly requested tags. If a privileged user has already assigned a reserved tag, an unprivileged topic owner cannot add an ordinary tag. [Topic editing](/app/src/posts/edit.js:134) similarly rejects an unchanged reserved tag in the submitted list. Check reserved-tag privileges for newly assigned tags while retaining whole-list tag-count validation.

**Tests:** `./node_modules/.bin/mocha test/topics.js --grep 'should reserve configured system tags for privileged users'` passed (1 passing), and `./node_modules/.bin/mocha test/topics.js` passed (165 passing).

**TEST_ENVIRONMENT_PROBLEM:** The first focused run failed before its assertions because Redis was unavailable at `127.0.0.1:6379`. A temporary local Redis server allowed both runs to complete; it was then stopped.