Implemented the confirmation state, TTL, resend eligibility, and cleanup changes in [src/user/email.js](/app/src/user/email.js).

`node --check src/user/email.js` passed. The existing email tests could not run because Redis at `127.0.0.1:6379` was unavailable; no test assertions executed.