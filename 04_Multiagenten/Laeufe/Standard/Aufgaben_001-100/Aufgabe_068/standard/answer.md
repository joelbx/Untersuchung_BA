Fixed the mail-details decryption path. Single and batch loads now carry supplied owner-encrypted session keys through the cache and apply them before decryption. Mail rendering, inbox rules, draft reply-to loading, and indexing now pass available mail keys.

Validation passed: TypeScript, 40 EntityRest tests, 29 MailIndexer tests, formatting, and `git diff --check`.