# Chat privacy issue checkpoint

- Objective: replace `restrictChat` with account chat privacy settings, enforce them for chat entry points, and add an idempotent upgrade.
- Findings: `User.saveSettings` persists account settings; `Messaging.canMessageUser` gates the API, but direct `Messaging.newRoom` and `addUsersToRoom` calls can bypass it. Account settings templates are supplied by installed themes, so the tracked controller custom settings section and client script are the integration points.
- Status: implemented normalized settings, ordered privacy checks, room creation and invite enforcement, account controls, API schema and labels, and a batched idempotent upgrade that removes the legacy field after migration.
- Verification: existing chat, user, and upgrade suites passed (363 tests); the targeted migration rerun passed after the legacy field cleanup. ESLint, JavaScript syntax checks, JSON/YAML parsing, and `git diff --check` passed.
