Task: Add global chat:privileged gate, profile canChat, OpenAPI/i18n, tests.
Status: implemented in checked-out files; no delegation used.
Implementation: global.can accepts string or array and preserves prior string hook shape; chat middleware/messaging use array checks; canMessageUser rejects privileged targets without chat:privileged; invitations use it; profile and v3 user responses expose canChat.
Evidence: messaging suite 80 passing; OpenAPI validation 1 passing; ESLint and git diff --check pass. Combined messaging/user/controllers run reached 455 passing then failed in controller user data export, with child process TypeError in src/user/jobs/export-profile.js:61 and assertion at test/controllers.js:1692.
Remaining: final review/report. Do not alter git history/index/harness.
