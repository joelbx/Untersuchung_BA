Implemented the privileged chat gate. `privileges.global.can` now returns a boolean for one privilege and a boolean array for an array. Chat requests accept either permission, while messaging checks require `chat:privileged` when the target is an administrator or moderator and return `[[error:no-privileges]]` when access is denied.

Added `canChat` to profile responses and the OpenAPI schema, and added the admin privilege label in English translations.

Validation: targeted ESLint, OpenAPI/locale parsing, and `git diff --check` passed. The existing messaging tests could not run because Redis was unavailable; the suite stopped during setup before any tests ran.