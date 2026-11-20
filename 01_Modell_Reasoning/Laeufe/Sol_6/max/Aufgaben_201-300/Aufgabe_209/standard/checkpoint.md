# Checkpoint

- Task: harden Subscribe to Calendar URL validation and centralize ResizeObserver test setup.
- Status: implementation complete; focused checks pass.
- Constraints: use local code and tests only; preserve git history, index baseline, and harness configuration.
- Changes: added `MAX_LENGTHS_API.CALENDAR_URL`; unified modal validation and warning priority; removed URL counter and input `maxLength`; placed one ResizeObserver mock in shared Jest setup and removed per-test assignments; added modal coverage with a default-export hook mock.
- Checks: modal spec (7 tests), subscribed calendars spec (1), calendar sidebar and main container specs (6), mail verification spec (12), mail tracker spec (11), components TypeScript check, ESLint with increased heap, Prettier, and `git diff --check` passed. The calendar tests printed existing React/router warnings.
