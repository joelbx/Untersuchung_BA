# Checkpoint

Task: Reject Python keywords in either segment of a fully qualified collection name.

Completed: Added `is_python_identifier` in the collection loader, made `AnsibleCollectionRef.is_valid_collection_name` check both segments, and routed Galaxy requirement parsing through it. Removed `_is_py_id`, `_is_fqcn`, and their compatibility code from `dataclasses.py`. Added unit and CLI regression cases.

Verification: 21 focused collection loader tests and 19 focused CLI tests passed. The full collection loader file passed (69 tests). A combined full run hit preexisting Galaxy class setup errors because no collection finder was installed in that test process; the focused CLI cases passed. `git diff --check` passed.
