# Checkpoint

- Task: Repair email confirmation storage and ACP validation actions/status in `/app`.
- Current state: Implemented UID-to-code mapping, explicit expiry, pending checks, fallback address lookup, force resend, code verification, deletion cleanup, and four ACP status labels. Added coverage in existing user, socket, and admin controller suites.
- Validation: Focused user confirmation suite (7 passing), admin socket validation suite (4 passing), ACP status test (1 passing), and user suite excluding a pre-existing invitation group test (208 passing). ESLint, locale JSON, diff check, and ACP template compilation pass.
- Existing unrelated failures: Full `test/user.js` stops at an invitation group test because its join call is commented out in `src/controllers/authentication.js`. Full `test/controllers-admin.js` stops at an existing 404 expectation for a missing user's edit/email page.
- Constraints: Use repository code and existing tests only; preserve git history, index, and harness configuration.
