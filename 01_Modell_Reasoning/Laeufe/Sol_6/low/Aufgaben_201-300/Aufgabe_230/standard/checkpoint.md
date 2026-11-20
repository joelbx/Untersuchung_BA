Task: expand affiliate queue identifier support and serialization.
Completed: PrioritizedIdentifier supports ISBN and ASIN strings, staging flag, identifier-based equality/hash, complete JSON dictionary, and compatibility alias/ISBN constructor. Queue deduplication and worker access use identifier.
Verification: scripts/tests/test_affiliate_server.py: 17 passed; git diff --check passed.
