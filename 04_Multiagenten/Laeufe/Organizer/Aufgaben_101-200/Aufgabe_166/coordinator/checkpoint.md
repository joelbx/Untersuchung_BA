# Checkpoint

Task: restore efficient vaulted variable file reads in DataLoader.load_from_file.
Status: implementation and focused tests complete.
Changes: `cache='none'` bypasses cache reads and writes; `cache='vaulted'` stores parsed vault files and reuses them; vars manager uses vaulted mode. Legacy boolean cache behavior remains available.
Validation: parsing DataLoader and variable manager unit test suites passed; `git diff --check` passed.
