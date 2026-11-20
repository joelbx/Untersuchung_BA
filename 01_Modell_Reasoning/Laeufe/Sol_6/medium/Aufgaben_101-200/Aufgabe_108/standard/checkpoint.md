# Cache abstraction checkpoint

Implemented typed `SimpleCache[V]` with fixed TTL expiry, loader behavior, active keys, and a private size-limited constructor. Migrated the HTTP client, genre repository, and play tracker off direct `ttlcache` use. Relevant package tests passed once; rerunning after strengthening expiry tests.
