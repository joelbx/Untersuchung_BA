# Checkpoint

Task: drop controller Python support through 3.11 and satisfy the collection archive extraction/install requirements.

Implemented: controller gate and ansible-test entry point require Python 3.12+, controller version metadata and test dependencies reflect that minimum, old importlib compatibility fallbacks were removed where no longer needed, and a changelog fragment was added. Collection extraction now calls `tar.getmember(dirname)` directly and no longer creates/reads `_ansible_normalized_cache`.

Verification: `test/units/cli/galaxy/test_collection_extract_tar.py` passed (3 tests), and `git diff --check` passed. Broader runs containing controller CLI modules cannot collect in this workspace because it runs Python 3.11.13, which the new minimum correctly rejects.
