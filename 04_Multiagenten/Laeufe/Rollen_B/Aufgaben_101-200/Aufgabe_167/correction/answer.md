Fixed the two review findings. `Subscribe` now compares each snapshot and digest captured together against the last digest it sent. Remote OCI stores now apply the configured authentication and insecure HTTP settings. I added regression tests for both cases.

Both exact test commands flagged by the reviewer pass. No remaining failures. TEST_ENVIRONMENT_PROBLEM: none.