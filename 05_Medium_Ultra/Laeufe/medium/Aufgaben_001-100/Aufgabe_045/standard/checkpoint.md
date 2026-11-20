# Checkpoint

Task: reject Python keywords and invalid identifiers in collection names.

Status: implementation complete. `AnsibleCollectionRef.is_valid_collection_name` now checks both segments as Python identifiers and rejects keywords; dependency resolution uses this check. Removed the legacy helpers and Python 2/3 compatibility block from `dataclasses.py`.

Verification: 71 collection loader tests passed; 7 new Galaxy resolver rejection cases passed. `git diff --check` passed. The broader Galaxy install suite cannot complete in this direct pytest invocation because its collection finder is not installed during fixture setup.
