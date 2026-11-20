Fixed the cache path for owner-encrypted session keys. Single and batch loads now retry cached entities with decryption errors when a key is supplied, and failed decryptions are no longer cached. Added regression tests for both paths.

The reviewer’s exact test filters passed: EntityRestClient 40/40, entity rest cache 112/112, and MailIndexer 29/29. The TypeScript check and `git diff --check` passed.

**TEST_ENVIRONMENT_PROBLEM:** The filtered runner still printed an unrelated `LoginFacadeTest` initialization error, but each run exited successfully with zero selected-test failures.