Task completed: Drive member and invitation data now keyed by shareId. Internal and external invitations have separate maps and share-scoped getters/actions. Member view reads and writes the active share only. Added getExistingEmails utility and focused isolation tests.
Validation: Jest focused + existing nearby suite 2 passed, 7 tests passed; drive-store TypeScript check passed; Prettier check passed; git diff --check passed.
No delegation used. Git history, index baseline, and harness configuration untouched.
