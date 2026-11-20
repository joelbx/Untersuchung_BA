# Checkpoint

Task: preserve safe internal collection symlinks during build and install.
Status: investigating repository paths and existing tests using assigned systematic debugging process.
Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using grep/find.

Root cause: `_build_collection_tar` passes `os.path.realpath` to `tar_file.add`, turning every link into target content. `_walk` follows symlink directories, duplicating children in FILES.json. Install always materializes file bytes and mkdirs directories. `_tarfile_extract` discards TarInfo.
Hypothesis: retain internal source link entries in tar and manifest, return TarInfo from extract helpers, then use resolved destination checks to restore safe links.

Implemented: preserve internal file and directory symlinks in tar with relative link targets; avoid manifest recursion into linked directories; keep external file links as copied regular files. Extract helpers now yield `(TarInfo, stream)`. Install recreates safe links and checks resolved parent/target paths; unsafe directory links become directories.
Regression evidence: updated symlink and helper tests failed before patch for expected reasons (three failures), then passed. Added build/install round trip and path safety tests. Final command: `PYTHONPATH=lib:test pytest -q --reruns 0 test/units/galaxy/test_collection.py test/units/galaxy/test_collection_install.py && git diff --check` exited 0, 103 passed.
