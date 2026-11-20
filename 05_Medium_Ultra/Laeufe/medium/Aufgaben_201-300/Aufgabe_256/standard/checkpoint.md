Task: Fix Play hosts validation and dynamic name derivation.
Status: Complete.
Changes: Play.load no longer derives or mutates name; Play.get_name derives it from hosts. Play._validate_hosts reports parser errors for empty, None, non-string sequence elements, and invalid scalar hosts, only when hosts was supplied. Exposed the existing sequence helper via ansible.utils.collection_loader. Updated unit coverage and the existing integration expectation.
Verification: 247 playbook unit tests passed; focused 16 tests passed after final edits; existing empty_hosts.yml syntax check returned the intended parser error; git diff --check passed.
Constraints respected: local code/tests only; git history and index baseline untouched.
