VERDICT: FIX

**Code defect:** [DefaultEntityRestCache.ts](/app/src/api/worker/rest/DefaultEntityRestCache.ts:230) returns cached entities without using a newly supplied key. Both the single and batch paths can also cache entities returned with decryption errors, so a later load with the mail’s key can still return undecrypted details. Reload cached entities with decryption errors when a key is supplied, and avoid caching failed decryptions.

**Tests:** From `/app/test`, `node --enable-source-maps test --filter EntityRestClient` passed (40/40); `node --enable-source-maps test --filter 'entity rest cache'` passed (108/108); and `node --enable-source-maps test --filter MailIndexer` passed (29/29). The TypeScript build passed.

**TEST_ENVIRONMENT_PROBLEM:** The runner printed unrelated `LoginFacadeTest` initialization errors during the first filtered run, although it exited successfully with zero selected-test failures. An initial invocation from `/app` failed because the test builder requires `/app/test` as its working directory.