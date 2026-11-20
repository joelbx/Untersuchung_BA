Task: implemented storage.readOnly metadata and validation, UI config selector/read-only state and storage icon badge, and non-database authentication bootstrap. Added configuration and authentication tests.
Checks: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/cmd` passed. `git diff --check` passed.
UI check blocked: command `npm run build` in /app/ui failed with `/bin/bash: line 1: npm: command not found` (exit 127). TypeScript compilation and UI tests remain unverified because Node tooling is unavailable; no dependencies were downloaded.
