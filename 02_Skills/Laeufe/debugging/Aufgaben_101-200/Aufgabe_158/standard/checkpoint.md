# Unarchive ZIP timestamp issue

Status: investigating root cause. Working tree was clean at start. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use grep/find.

Plan: inspect ZIP timestamp handling and existing tests; reproduce the failure before changing implementation; make one focused fix; run relevant existing tests.

Root cause: `ZipArchive.is_unarchived` parses the `zipinfo -T` timestamp with `time.strptime` and constructs `datetime.datetime`. A ZIP entry with zero month/day yields `19800000.000000`; `strptime` raises before extraction can be considered. The path is reached when the destination member exists. Working pattern elsewhere in this module is to validate parsed archive metadata before comparing it. Hypothesis: validating the fixed-width date fields and falling back to the 1980 ZIP epoch will allow normal comparison and extraction for malformed entries.

Reproduction: `PYTHONPATH=lib python -m pytest -q test/units/modules/test_unarchive.py -k 'valid_time_stamp or invalid_timestamp_on_existing_file'` failed before the fix. The integration-style unit case reached `is_unarchived` with an existing member and raised the reported `ValueError`; the helper cases failed because `_valid_time_stamp` did not exist.

Fix: `ZipArchive._valid_time_stamp` extracts fixed-width date fields with a regular expression, enforces ZIP years 1980–2107, validates calendar and clock fields with `datetime`, and returns the required epoch tuple for invalid values. `is_unarchived` now passes its result to `time.mktime`.

Verification: `PYTHONPATH=lib python -m pytest -q test/units/modules/test_unarchive.py --reruns 0` passed (13 tests). `git diff --check` passed. No offline tooling blockage beyond missing `rg`; no downloads attempted.
