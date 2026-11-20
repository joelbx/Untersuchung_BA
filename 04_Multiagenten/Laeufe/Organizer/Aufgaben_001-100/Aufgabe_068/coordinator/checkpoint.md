Task: Propagate optional owner-encrypted session keys through single and batch entity loaders, cache, and mail detail call sites before decryption.
Status: Implemented and verified. No delegation used.
Changes: EntityClient, EntityRestInterface/Client, DefaultEntityRestCache, MailUtils, InboxRuleHandler, MailFacade, MailIndexer. Added REST client and cache propagation tests and updated omitted-map argument assertion.
Verification: Test build/type check passed; focused suites EntityRestClient 40, entity rest cache 110, MailIndexer 29, MailFacade 17, MailModel 26 tests passed with zero failures. Targeted eslint and git diff --check passed.
Constraints: Local code/tests only; no git history, index baseline, or harness configuration changed.
