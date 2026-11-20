Task: Delete uploads exclusive to purged posts, with an ACP preservation setting and safe deletion API.
Status: Implemented orphan upload deletion on post purge, safe single/list disk deletion, ACP preservation setting, and topic thumbnail preservation during topic purge. Added coverage for exclusive, shared, preserved, topic, and invalid-path cases.
Verification: ESLint passed; 71 relevant Mocha tests passed; git diff --check passed. Local Redis was started for the test suite.
