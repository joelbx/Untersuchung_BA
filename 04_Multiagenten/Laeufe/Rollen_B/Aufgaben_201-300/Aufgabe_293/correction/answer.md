I found no concrete code defect in the checked-out OCI patch, so I made no source changes in this correction round. The reviewer’s exact Go test command and `git diff --check` passed.

**TEST_ENVIRONMENT_PROBLEM:** The `fs/oci` integration command could not run because `mage` is unavailable here; it exited 127. That suite remains unverified and needs to run in the configured CI environment.