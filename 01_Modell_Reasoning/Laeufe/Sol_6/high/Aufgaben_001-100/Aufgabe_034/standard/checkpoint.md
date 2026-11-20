# Checkpoint

Task: normalize Internet Archive ISBN and publisher metadata in Open Library records.
Status: complete. Added public ISBN and publisher/place utilities; wired them into `get_ia_record` and updated existing tests.
Verification: 30 focused tests passed; 18 import API tests passed; `git diff --check` passed. Black is unavailable in the local environment.
Constraints observed: local repository and tests only; repository history and index unchanged.
