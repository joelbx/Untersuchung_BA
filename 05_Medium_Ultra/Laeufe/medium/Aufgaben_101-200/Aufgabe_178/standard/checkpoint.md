Task: Add bcrypt ident support to password_hash filter and password lookup.
Status: Implemented and verified.
Changes: Threaded ident through filter and hash backends; persisted bcrypt ident with salt in password lookup; defaulted lookup bcrypt to 2a; documented usage and added focused tests. For legacy $2$, crypt uses native support where present and passlib fallback where available.
Verification: PYTHONPATH=lib python -m pytest -q test/units/utils/test_encrypt.py test/units/plugins/lookup/test_password.py (54 passed); git diff --check (clean).
Limitation: A crypt-only host whose crypt library rejects $2$ cannot generate that variant.
