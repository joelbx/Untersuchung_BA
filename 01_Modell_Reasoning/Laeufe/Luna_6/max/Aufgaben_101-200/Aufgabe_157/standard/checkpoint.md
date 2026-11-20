# Checkpoint

Task: standardize mail metrics label identifiers and page size values, add the `@proton/metrics` dependency, and update the lockfile.

Status: complete. Added `mailMetricsHelper.ts` with custom label/folder normalization and page size normalization. Added `@proton/metrics` to the mail app manifest and updated the mail workspace lock entry. The mail app typecheck passed; the existing labels helper test passed all 24 cases; `git diff --check` passed.
