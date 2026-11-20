# Checkpoint

Implemented collection symlink preservation and safe extraction in `lib/ansible/galaxy/collection.py`.

- Manifest walking now records a symlink as one entry and does not recurse through linked directories.
- Tar builds preserve in-collection links with relative link targets; external file links are archived as regular files.
- Tar member context helpers now yield `(TarInfo, readable_stream)`.
- Artifact install recreates only in-destination symlinks, using dedicated file and directory extraction paths.
- Updated existing unit expectations for the new manifest and tar helper behavior.

Validation: `python -m pytest -q test/units/galaxy/test_collection.py test/units/galaxy/test_collection_install.py` passed (100 tests); `git diff --check` passed.
