Issue: make Ansible collection manifest configuration more flexible and distinguish an absent manifest from explicit empty/null values.

Initial findings: `_build_files_manifest` currently uses truthiness to decide whether distlib controls apply, and rejects ignore patterns with a truthy manifest. The walk implementation handles symlink policy and emits the regular files manifest. Existing unit coverage is in `test/units/galaxy/test_collection.py`.

Next: inspect manifest loading and walk behavior, change absent-manifest handling using `ansible.utils.sentinel.Sentinel`, cover required cases, and run relevant existing unit tests.
