Implemented symlink preservation and safe extraction in [collection.py](/app/lib/ansible/galaxy/collection.py:773). Internal links are archived with relative targets and restored only when they resolve inside the destination; external file links are materialized as regular files. Manifest walking no longer traverses symlinked directories, and tar helpers expose the `TarInfo` with a readable stream.

Updated coverage in [test_collection.py](/app/test/units/galaxy/test_collection.py:492).

- Collection tests: **62 passed**
- Collection install tests: **41 passed**
- `git diff --check`: clean