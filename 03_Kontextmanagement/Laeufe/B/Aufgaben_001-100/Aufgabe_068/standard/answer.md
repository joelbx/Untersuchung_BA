Implemented owner-encrypted session key propagation through the single and batch loaders, cache, and Mail details call sites. Keys are applied before decryption; batch calls still accept a fourth argument of `undefined`.

Validation passed: TypeScript type check, relevant rest client and cache tests, MailIndexer and MailFacade tests, and `git diff --check`. The repository issue is complete.