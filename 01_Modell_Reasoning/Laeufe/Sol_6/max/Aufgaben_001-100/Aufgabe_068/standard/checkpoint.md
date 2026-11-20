Task: Propagate caller-provided owner-encrypted session keys through entity loads, caches, and mail details call sites before decryption.

Status: Complete. Optional key propagation runs through EntityClient, EntityRestClient, DefaultEntityRestCache, MailUtils, InboxRuleHandler, MailFacade, and MailIndexer. Fetched literals receive Base64-encoded keys before session-key resolution and entity mapping. Cache reloads previously failed decryption results when a key is supplied.

Verification: Root TypeScript check, changed-file Prettier and ESLint checks, and git diff check pass. Relevant tests pass: EntityRestClient (41), entity rest cache ephemeral/offline (108), loadMailDetails (2), MailFacade (18), MailIndexer (29), InboxRuleHandler (6). The test runner emits unrelated LoginFacade skipped-spec initialization warnings, but reported zero failing tests for these suites.

Constraints: Use local repository and existing tests only; leave git history, index, and harness configuration unchanged.
