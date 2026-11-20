Task: Fix Play hosts validation and dynamic name derivation for malformed hosts.
Status: Complete.
Changes: Play.load no longer derives/mutates name; Play.get_name derives it dynamically; _validate_hosts reports parser errors for empty, null, invalid sequence members, and invalid scalar types only when hosts is present. Exposed the existing is_sequence helper through ansible.utils.collection_loader for the required import. Updated unit coverage and the existing integration expectation.
Verification: PYTHONPATH=lib:test python -m pytest -q test/units/playbook (247 passed); git diff --check passed; ansible-playbook --syntax-check on existing empty_hosts fixture emitted the expected parser error and exited 4.
