# Checkpoint

Task: Propagate a parent mail's owner-encrypted session key through entity loading, cache layers, and mail detail call sites.

Completed:
- Added optional single and batch key parameters to entity client interfaces and forwarded them through `DefaultEntityRestCache`.
- Applied provided key bytes to loaded entities before session key resolution and decryption.
- Ensured keyed loads bypass cached detail instances so decryption receives the supplied key.
- Passed mail keys from mail detail, reply-to, indexing, and inbox-rule loading paths.
- Kept old argument shapes when optional keys are absent.

Validation:
- `npm run types -- --pretty false` passed.
- Existing EntityRestClient tests passed: 38 passing, 0 failing.
- Existing entity rest cache tests passed: 106 passing, 0 failing.
- Existing MailIndexer tests passed: 29 passing, 0 failing.
- Existing InboxRuleHandler tests passed: 6 passing, 0 failing.
- Prettier check and `git diff --check` passed.
