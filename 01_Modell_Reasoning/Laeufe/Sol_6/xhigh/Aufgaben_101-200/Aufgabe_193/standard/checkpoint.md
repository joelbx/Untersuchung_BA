Task: Unify ansible-galaxy requirements installs for roles and collections.
Status: Implemented mixed requirements installation with separate role and collection helpers, path-aware skip messages, empty-file handling, and dependency processing fixes.
Verification: ansible-galaxy CLI unit tests passed (122 tests) with ANSIBLE_DEVEL_WARNING=False. Updated the existing integration assertion for empty requirements; integration execution requires external Galaxy access and was not run.
Constraints: Use local code and tests only; preserve git history, index, and harness configuration.
