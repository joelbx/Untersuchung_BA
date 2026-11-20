Fixed the crypt-backed BCrypt path for `ident='2'`: when the host’s `crypt` rejects `$2$`, it uses passlib to generate the hash. Added an unmocked regression test for the reported failure.

The reviewer’s test commands pass: **50 hashing and lookup tests** and **7 filter tests**. No remaining test failures. On hosts where crypt rejects `$2$`, this variant requires passlib to be installed.