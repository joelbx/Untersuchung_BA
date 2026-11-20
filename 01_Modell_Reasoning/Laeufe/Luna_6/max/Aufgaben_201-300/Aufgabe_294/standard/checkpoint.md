# Checkpoint

Implemented collection symlink preservation and safe extraction in `lib/ansible/galaxy/collection.py`.

Changes:
- `_is_child_path` checks resolved paths with path-boundary-safe containment.
- `_walk` records symlinks once and does not recurse through directory symlinks. External directory links remain skipped; external file links are recorded as files.
- `_build_collection_tar` writes internal links as symlink members with relative targets and copies external file link contents as regular members.
- `_tarfile_extract` and `_get_tar_file_member` expose `(TarInfo, stream)`; dangling links are handled without following an absent archive target.
- Install now extracts directory entries through `_extract_tar_dir` and file entries through `_extract_tar_file`, restoring links only when their resolved targets stay inside the collection destination and flattening unsafe links.
- Updated existing expectations and added build, extraction, and install coverage in `test/units/galaxy/test_collection.py`.

Verification completed:
- `PYTHONPATH=lib:test pytest -q test/units/galaxy` — 153 passed.
- `python -m py_compile lib/ansible/galaxy/collection.py test/units/galaxy/test_collection.py` — passed.
- `git diff --check` — passed.
