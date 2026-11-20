# Checkpoint

Implemented owner-encrypted session key propagation through EntityClient, DefaultEntityRestCache, and EntityRestClient. The REST loaders attach supplied keys to response literals before session-key resolution and decryption. Mail detail call sites, including indexing and inbox rules, pass the mail key. Cache entries with decryption errors are fetched again when a key is supplied. Added focused REST loader and cache tests, including the explicit undefined fourth argument assertion.

Verification: `npm run types -- --pretty false` passed; filtered EntityRestClient tests passed (40); filtered entity rest cache tests passed (108); `git diff --check` passed.
