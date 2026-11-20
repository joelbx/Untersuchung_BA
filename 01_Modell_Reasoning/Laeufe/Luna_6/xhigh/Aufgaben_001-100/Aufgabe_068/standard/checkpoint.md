# Checkpoint

Task: propagate optional owner-encrypted session keys through entity single/batch loading, cache layers, and mail details loader call sites so entities decrypt before use.

Completed:
- Single entity loads accept a parent mail's optional owner-encrypted session key and attach it to the raw instance before session-key resolution.
- Batch loads accept a map keyed by element id and attach each matching key before decryption.
- `EntityClient` and `DefaultEntityRestCache` forward the new parameters. Cache calls without a batch map retain the previous three-argument underlying call shape.
- Mail details loads in mail utilities, the mail facade, inbox rules, and search indexing pass the mail key when available.

Verification:
- `npm run types` passed.
- Focused existing tests passed: EntityRestClient (38), entity rest cache (106), MailIndexer (29), MailFacade (17), InboxRuleHandler (6), MailUtilsSignature (8).
- Prettier check and `git diff --check` passed.
