`Edition.from_isbn` now parses and loads matching staged data locally, then updates the import item’s status and returns the edition. It no longer sends that match through the import endpoint. I added a regression test for the local path.

The reviewer’s test modules passed: **17 tests**. `git diff --check` passed. No remaining failures or test environment problems.