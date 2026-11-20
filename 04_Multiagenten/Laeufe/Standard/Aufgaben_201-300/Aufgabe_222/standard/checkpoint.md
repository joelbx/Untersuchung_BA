Status: complete; extracted RoleMixin._build_doc and updated _create_role_doc to consume its tuple.
Verification: PYTHONPATH=/app/lib python -m pytest test/units/cli/test_doc.py -q (17 passed); git diff --check passed.
