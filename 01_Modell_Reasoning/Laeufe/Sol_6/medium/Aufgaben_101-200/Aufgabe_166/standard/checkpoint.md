Task: Restore efficient vaulted variable file reads in DataLoader.load_from_file.
Status: Implemented `cache='none'` and vault-only caching in DataLoader; vars_files now uses vault-only caching. Added regression tests for vaulted and plain files. Relevant tests passed: 41 tests in test_dataloader.py and test_variable_manager.py. `git diff --check` passed.
