Fixed owner-encrypted session key propagation through single and batch loaders, the cache, and mail detail callers. The key is applied before decryption, and cached details with decryption errors are retried when a key is supplied. The path does not require the crypto layer’s session-key cache.

Relevant suites passed: 204 tests, 0 failures. TypeScript, Prettier, ESLint, and diff checks passed.