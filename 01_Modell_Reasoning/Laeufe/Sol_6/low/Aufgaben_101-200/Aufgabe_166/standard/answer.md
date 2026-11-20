Updated `DataLoader.load_from_file` so `cache='none'` leaves the file cache empty, while `cache='vaulted'` stores parsed vaulted files and reuses them on later loads. Playbook variable files now use vaulted caching.

The relevant existing tests pass: 33 loader tests and 8 variable manager tests.