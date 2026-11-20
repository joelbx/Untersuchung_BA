Propagated the mail’s owner-encrypted session key through single and batch loads, the entity cache, and the mail detail call sites. The REST client applies each supplied key before decryption. Added regression tests for key injection and cache forwarding, including the omitted batch-map argument.

The test build and type check passed. Focused suites passed with zero failures: REST client (40), entity cache (110), MailIndexer (29), MailFacade (17), and MailModel (26). Targeted ESLint and `git diff --check` also passed.

No delegation was used.