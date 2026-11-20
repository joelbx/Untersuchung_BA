Task: restore efficient vaulted vars file caching in DataLoader.load_from_file.
Status: complete.
Changes: cache none bypasses writes; cache vaulted stores decrypted parsed files; vars manager uses vaulted mode.
Verification: dataloader 33 passed; variable manager 8 passed; git diff --check clean.
