Implemented ZIP based cover archival, normalized archive.org URL and batch path helpers, upload checks, batch finalization, and the `failed`/`uploaded` schema columns with indexes. Updated cover serving to use ZIP URLs for the affected ID range.

Verification: `pytest -q openlibrary/coverstore/tests` passed (18 passed, 7 skipped); Python compilation succeeded.

The existing archive test is skipped in this environment, so the full archive workflow was not exercised.