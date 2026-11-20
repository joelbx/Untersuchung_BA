Fixed the reviewer’s immutability finding. File extended attributes now expose deeply readonly fields, and creation freezes the result and its nested values at runtime. I added a regression test for the frozen structure.

The focused Drive Jest suite passed (5/5), the Drive TypeScript check passed, and `git diff --check` found no issues. No remaining failures or test environment problems.