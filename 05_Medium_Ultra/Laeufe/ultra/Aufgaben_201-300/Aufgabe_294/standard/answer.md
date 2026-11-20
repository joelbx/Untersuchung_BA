Updated [collection.py](/app/lib/ansible/galaxy/collection.py) so builds preserve internal file and directory symlinks with relative targets, copy external file links as regular files, and avoid expanding linked directories in the manifest. Installation now restores links only when their targets resolve within the collection destination; tar helpers expose both the member and its stream.

Three subagents helped update [build tests](/app/test/units/galaxy/test_collection.py), add [install and safety tests](/app/test/units/galaxy/test_collection_install.py), and review the patch. **All 156 Galaxy unit tests pass**, as do `git diff --check` and Python compilation.

If a link’s target was excluded from the tar, install restores the safe link, but cannot verify the target content checksum.