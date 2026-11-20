# Checkpoint

Task: support minimal or absent Ansible collection manifest configuration while preserving ignore and symlink behavior.
Status: complete.
Implementation: absent manifest uses Sentinel; explicit empty mapping and null select manifest directives; external file and directory symlinks are excluded by the walker.
Verification: PYTHONPATH=/app/lib python -m pytest -q -o addopts= test/units/galaxy/test_collection.py test/units/galaxy/test_collection_install.py (124 passed); git diff --check passed.
Delegation: none.
