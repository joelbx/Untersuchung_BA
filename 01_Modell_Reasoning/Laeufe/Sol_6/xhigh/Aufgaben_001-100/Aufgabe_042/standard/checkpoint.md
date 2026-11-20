Task: Add WebFinger endpoint at /.well-known/webfinger.
Status: Controller, router, core registration, and integration tests added. ESLint, syntax checks, git diff check, and isolated handler checks pass. Targeted Mocha cannot start because the configured Redis server refuses connection at 127.0.0.1:6379.
Constraints: Edit checked-out files only; preserve git history, index baseline, and harness configuration. Use local code/tests only.
