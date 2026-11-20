# Checkpoint

Task: preserve safe internal collection symlinks in build/install and expose tar members from extract helpers.

Status: implementation and focused tests complete. Internal file and directory links are archived with relative targets, manifests avoid walking linked directories, external file links are copied, extraction validates destination and target paths, and tar helpers expose TarInfo with the stream.

Verification: `python -m pytest -q test/units/galaxy/test_collection.py` passed (63 tests); `git diff --check` passed. Combined collection and CLI unit run passed 169 tests and had four CLI warning-count failures; the same CLI tests fail independently, so they are unrelated to collection symlink paths.
