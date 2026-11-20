Implemented symlink preservation for collection builds and safe symlink restoration during installs in [collection.py](/app/lib/ansible/galaxy/collection.py:955). Internal file and directory links are archived with relative targets; external file links are copied as regular files. Extraction helpers now expose the `TarInfo` and stream, and install checks resolved paths before restoring links.

Updated and added coverage in [test_collection.py](/app/test/units/galaxy/test_collection.py:492).

**Verification:** `PYTHONPATH=lib:test pytest -q test/units/galaxy` passed (153 tests); `py_compile` and `git diff --check` passed.