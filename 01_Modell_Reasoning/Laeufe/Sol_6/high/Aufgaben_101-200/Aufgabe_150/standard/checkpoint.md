Task: Make Ansible collection manifest configuration accept minimal values and ensure absent manifest uses Sentinel correctly.
Status: Complete. Missing manifest metadata now uses Sentinel; explicit {} and null enable default manifest directives. The Sentinel path preserves build_ignore and excludes external file and directory symlinks while retaining internal links.
Files edited: lib/ansible/galaxy/collection/__init__.py; lib/ansible/galaxy/collection/concrete_artifact_manager.py; test/units/galaxy/test_collection.py; docs/docsite/rst/dev_guide/developing_collections_distributing.rst.
Validation: PYTHONPATH=lib pytest -q test/units/galaxy (214 passed); git diff --check passed. Optional distlib is absent locally, so directive execution was not exercised.
