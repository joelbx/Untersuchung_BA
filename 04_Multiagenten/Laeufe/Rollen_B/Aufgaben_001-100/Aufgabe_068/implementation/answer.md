Updated the single and batch loaders, including `DefaultEntityRestCache`, to pass supplied owner-encrypted session keys to `EntityRestClient`. The client attaches each key to the raw entity before decryption. Mail detail callers and the indexer now supply the parent mail’s key.

TypeScript checking and the focused EntityRestClient, cache, and MailIndexer test suites passed.