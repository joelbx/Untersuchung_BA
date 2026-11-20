Task: restore efficient vaulted vars file reads in DataLoader.load_from_file.
Status: implemented cache='none' bypass and cache='vaulted' for encrypted files; play vars_files now uses vaulted caching.
Validation: DataLoader unit tests (33 passed), variable manager unit tests (8 passed), git diff --check clean.
