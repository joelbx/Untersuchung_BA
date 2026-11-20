Implemented `chat:privileged` across chat permission checks. Starting or inviting a privileged user without it now returns `[[error:no-privileges]]`. The profile API exposes a boolean `canChat`, documented in the [OpenAPI schema](/app/public/openapi/components/schemas/UserObject.yaml).

Verification passed: 94 messaging and middleware tests, ESLint, and schema and translation parsing.