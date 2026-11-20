Updated the repository to require Python 3.12 or newer on the controller. Both user-facing entry points now show the same version error; packaging metadata and the changelog reflect the change. Python 3.10 and 3.11 remain listed for managed targets.

Collection installation no longer uses the private TarFile cache. `_extract_tar_dir` passes `dirname` unchanged to `getmember()` and raises the specified `AnsibleError` when the member is missing. I also removed controller compatibility branches made obsolete by the new minimum.

Verification: 159 relevant unit tests passed and 1 was skipped. Both entry points rejected Python 3.11 with identical messages. The test runner has only Python 3.11, so the unit tests ran with the import gate bypassed in memory; they were not run under Python 3.12.