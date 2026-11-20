Fixed vaulted vars file caching. `cache='none'` now leaves the file cache untouched; `cache='vaulted'` caches parsed vaulted files and reuses them on later loads. Play vars files now use vaulted-only caching.

Verification: 44 affected unit tests passed, including a test that loads the same vaulted play vars file twice and observes one file read. `git diff --check` passed.